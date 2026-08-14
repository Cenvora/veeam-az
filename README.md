<h1 align="center">
<br>
<img src="https://raw.githubusercontent.com/Cenvora/veeam-az/main/media/Veeam_logo_2024_RGB_main_20.png"
     alt="Veeam Logo"
     height="100">
<br>
<br>
Veeam Backup for Azure Python API Wrapper
</h1>

<h4 align="center">
Python package for interacting with the Veeam Backup for Azure REST API
</h4>

<!-- Summary -->
This project is an independent, open source Python client for the Veeam Backup for Azure <a href="https://helpcenter.veeam.com/references/vbazure/8.1/rest/main/tag/SectionAbout/index.html">REST API</a>. It is not affiliated with, endorsed by, or sponsored by Veeam Software.
<!-- Summary -->

## Supported Versions

<table>
  <thead>
    <tr>
      <th>VBA Version</th>
      <th>API Version</th>
      <th>Supported</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>8.1</td>
      <td>8.1</td>
      <td style="text-align:center;">&#9989;</td>
    </tr>
    <tr>
      <td>&lt; 8.1</td>
      <td>&lt; 8.1</td>
      <td style="text-align:center;">&#10060;</td>
    </tr>
  </tbody>
</table>

## How to support new API versions
1. Download the OpenAPI schema into openapi_schemas
2. Install the openapi-python-client package
3. Run `python fix_openapi_schema.py .\openapi_schemas\vbaz_rest_{version}.json .\openapi_schemas\vbaz_rest_{version}_fixed.json` 
4. Run `openapi-python-client generate --path ".\openapi_schemas\vbaz_rest_{version}_fixed.json" --output-path ".\veeam_az" --overwrite`
5. Fix any warnings/errors
6. Rename the folder to match the API version (i.e., `v8_1`)
7. Add the version mapping to versions.py
8. Write pytest tests
9. If an older API has been deprecated, delete its folder, json, and version.py entry, then update the supported versions section of the readme

## Install
### From PyPi
`pip install veeam-az`


### From Source
Clone the repository and install dependencies:
```sh
git clone https://github.com/Cenvora/veeam-az.git
cd veeam-az
pip install -e .
```

## Usage
### Recommended Usage (Smart Client)
The `VeeamClient` handles:
- API version routing
- Authentication (username/password or bearer token)
- Token refresh (password-based auth automatically re-authenticates on expiry)
- Async calls
- Operation discovery

Each packaged version can be called independently through separate imports, but this is the <strong>recommended way</strong>  to use this library.

#### Create a client and connect
```python
import asyncio
from veeam_az import VeeamClient

async def main():
    vc = VeeamClient(
        host="https://vbaz.example.com",
        username="administrator",
        password="SuperSecretPassword",
        api_version="8.1",
        verify_ssl=False,
    )

    await vc.connect()

    # use the client...

    await vc.close()

asyncio.run(main())
```

You can also authenticate with a pre-existing bearer token instead of a
username/password. Token-based clients skip the login call and are never
refreshed automatically:
```python
vc = VeeamClient(
    host="https://vbaz.example.com",
    token="eyJhbGciOi...",
    api_version="8.1",
    verify_ssl=False,
)
await vc.connect()
```

#### Detect the API version an appliance serves

The REST API has no endpoint that reports its supported versions, and nothing negotiates one
for you — the version is part of every path, so a client picks one up front. That path is
also what makes detection possible: `/api/v{version}/system/about` requires a token, so an
anonymous probe gets 401 where the version is served and 404 where it is not.
`detect_api_version` returns the newest version that both the appliance serves and this
library can speak:

```python
import asyncio
from veeam_az import VeeamClient
from veeam_az.discovery import detect_api_version

async def main():
    base_url = "https://vbaz.example.com"

    api_version = await detect_api_version(base_url, verify_ssl=False)
    if api_version is None:
        # The appliance may be unreachable or behind a proxy — choose your own default
        api_version = "8.1"

    vc = VeeamClient(
        host=base_url,
        username="administrator",
        password="SuperSecretPassword",
        api_version=api_version,
        verify_ssl=False,
    )
    await vc.connect()

asyncio.run(main())
```

Detection needs no credentials, so it can run before you have any. Probes are concurrent, so
it costs roughly one round trip regardless of how many versions this library supports.

If the appliance is not on the usual HTTPS port, `detect_rest_api` finds the port and the
version at once:

```python
from veeam_az.discovery import detect_rest_api

endpoint = await detect_rest_api("vbaz.example.com", ports=(443, 8443), verify_ssl=False)
if endpoint:
    print(endpoint.port, endpoint.api_version)  # e.g. 443 8.1
    base_url = f"https://vbaz.example.com{endpoint.base_url_suffix}"
```

Resolve it once and store the result rather than detecting on every start: an appliance
upgrade would otherwise silently move you onto a newer version, and versions rename enum
values and add required fields.

#### Call an API endpoint (async)
```python
policies = await vc.call(
    vc.api("policy").policy_get_policies
)
```

#### Call any endpoint
Operations map directly to the OpenAPI layout. Each tag becomes a namespace
folder and each operation becomes a module:
```markdown
api/
└── policy/
    └── policy_get_policies.py
```

Call it via the namespace:
```python
await vc.call(
    vc.api("policy").policy_get_policies
)
```

Or explicitly, with the operation on the same line:
```python
await vc.call(
    vc.api("policy.policy_get_policies")
)
```

Pass endpoint arguments as keyword arguments to `call`:
```python
repo = await vc.call(
    vc.api("repository").repository_get_repository,
    repository_id="<repository-id>",
)
```

#### Pagination example
List endpoints accept `offset` and `limit`:
```python
result = await vc.call(
    vc.api("policy").policy_get_policies,
    limit=50,
    offset=0,
)
```

#### Close the client
```python
await vc.close()
```

## Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a feature branch
- Make your changes and add tests
- Submit a pull request with a clear description

Please follow PEP8 style and include docstrings for new functions/classes.

## 🤝 Core Contributors
This project is made possible thanks to the efforts of our core contributors:

- [Jonah May](https://github.com/JonahMMay)  
- [Maurice Kevenaar](https://github.com/mkevenaar)  

We’re grateful for their continued support and contributions.
