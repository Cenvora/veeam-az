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
