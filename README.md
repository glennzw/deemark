# deemark: DMARC API

A quick, simple wrapper around https://github.com/domainaware/checkdmarc using [FastAPI](https://github.com/tiangolo/fastapi) to query DMARC records for a given domain.

Heroku deployment: https://deemark.herokuapp.com/api/checkdmarc/whitehouse.gov

Run locally:

```
$ uvicorn main:app 
```

```
$ curl http://localhost:5000/api/checkdmarc/fbi.gov

{
  "domain": "fbi.gov",
  "base_domain": "fbi.gov",
  "dnssec": true,
  "ns": {
    "hostnames": [
      "ns-cloud-e1.googledomains.com",
      "ns-cloud-e2.googledomains.com",
      "ns-cloud-e3.googledomains.com",
      "ns-cloud-e4.googledomains.com"
    ],
    "warnings": []
  },
  "mx": {
    "hosts": [
      {
        "preference": 10,
        "hostname": "mx-east.fbi.gov",
        "addresses": [
          "153.31.160.5"
        ],
        "tls": true,
        "starttls": true
      },
      {
        "preference": 20,
        "hostname": "mx-west.fbi.gov",
        "addresses": [
          "153.31.192.5"
        ],
        "tls": true,
        "starttls": true
      }
    ],
    "warnings": [
      "The reverse DNS of 153.31.160.5 is 5.160.31.153.in-addr.arpa, but the A/AAAA DNS records for 5.160.31.153.in-addr.arpa do not resolve to 153.31.160.5",
      "The reverse DNS of 153.31.192.5 is 5.192.31.153.in-addr.arpa, but the A/AAAA DNS records for 5.192.31.153.in-addr.arpa do not resolve to 153.31.192.5"
    ]
  },
  "spf": {
    "record": "v=spf1 +mx ip4:153.31.0.0/16 -all",
    "valid": true,
    "dns_lookups": 1,
    "warnings": [],
    "parsed": {
      "pass": [
        {
          "value": "mx-east.fbi.gov",
          "mechanism": "mx"
        },
        {
          "value": "mx-west.fbi.gov",
          "mechanism": "mx"
        },
        {
          "value": "153.31.0.0/16",
          "mechanism": "ip4"
        }
      ],
      "neutral": [],
      "softfail": [],
      "fail": [],
      "include": [],
      "redirect": null,
      "exp": null,
      "all": "fail"
    }
  },
  "dmarc": {
    "record": "v=DMARC1; p=reject; rua=mailto:dmarc-feedback@fbi.gov,mailto:reports@dmarc.cyber.dhs.gov; ruf=mailto:dmarc-feedback@fbi.gov; pct=100",
    "valid": true,
    "location": "fbi.gov",
    "warnings": [],
    "tags": {
      "v": {
        "value": "DMARC1",
        "explicit": true,
        "name": "Version",
        "description": "Identifies the record retrieved as a DMARC record. It MUST have the value of \"DMARC1\". The value of this tag MUST match precisely; if it does not or it is absent, the entire retrieved record MUST be ignored. It MUST be the first tag in the list."
      },
      "p": {
        "value": "reject",
        "explicit": true,
        "name": "Requested Mail Receiver Policy",
        "description": "The Domain Owner wishes for Mail Receivers to reject email that fails the DMARC mechanism check. Rejection SHOULD occur during the SMTP transaction."
      },
      "rua": {
        "value": [
          {
            "scheme": "mailto",
            "address": "dmarc-feedback@fbi.gov",
            "size_limit": null
          },
          {
            "scheme": "mailto",
            "address": "reports@dmarc.cyber.dhs.gov",
            "size_limit": null
          }
        ],
        "explicit": true,
        "name": "Aggregate Feedback Addresses",
        "description": " A comma-separated list of DMARC URIs to which aggregate feedback is to be sent."
      },
      "ruf": {
        "value": [
          {
            "scheme": "mailto",
            "address": "dmarc-feedback@fbi.gov",
            "size_limit": null
          }
        ],
        "explicit": true,
        "name": "Forensic Feedback Addresses",
        "description": " A comma-separated list of DMARC URIs to which forensic feedback is to be sent."
      },
      "pct": {
        "value": 100,
        "explicit": true,
        "name": "Percentage",
        "default": 100,
        "description": "Integer percentage of messages from the Domain Owner's mail stream to which the DMARC policy is to be applied. However, this MUST NOT be applied to the DMARC-generated reports, all of which must be sent and received unhindered. The purpose of the \"pct\" tag is to allow Domain Owners to enact a slow rollout of enforcement of the DMARC mechanism."
      },
      "adkim": {
        "value": "r",
        "explicit": false,
        "name": "DKIM Alignment Mode",
        "default": "r",
        "description": "In relaxed mode, the Organizational Domains of both the DKIM-authenticated signing domain (taken from the value of the \"d=\" tag in the signature) and that of the RFC 5322 From domain must be equal if the identifiers are to be considered aligned."
      },
      "aspf": {
        "value": "r",
        "explicit": false,
        "name": "SPF alignment mode",
        "default": "r",
        "description": "In relaxed mode, the SPF-authenticated domain and RFC5322 From domain must have the same Organizational Domain. In strict mode, only an exact DNS domain match is considered to produce Identifier Alignment."
      },
      "fo": {
        "value": [
          "0"
        ],
        "explicit": false,
        "name": "Failure Reporting Options",
        "default": "0",
        "description": "0: Generate a DMARC failure report if all underlying authentication mechanisms fail to produce an aligned \"pass\" result."
      },
      "rf": {
        "value": [
          "afrf"
        ],
        "explicit": false,
        "name": "Report Format",
        "default": "afrf",
        "description": "afrf:  \"Authentication Failure Reporting Using the Abuse Reporting Format\", RFC 6591, April 2012,<http://www.rfc-editor.org/info/rfc6591>"
      },
      "ri": {
        "value": 86400,
        "explicit": false,
        "name": "Report Interval",
        "default": 86400,
        "description": "Indicates a request to Receivers to generate aggregate reports separated by no more than the requested number of seconds. DMARC implementations MUST be able to provide daily reports and SHOULD be able to provide hourly reports when requested. However, anything other than a daily report is understood to be accommodated on a best-effort basis."
      },
      "sp": {
        "value": "reject",
        "explicit": false,
        "name": "Subdomain Policy",
        "description": "Indicates the policy to be enacted by the Receiver at the request of the Domain Owner. It applies only to subdomains of the domain queried, and not to the domain itself. Its syntax is identical to that of the \"p\" tag defined above. If absent, the policy specified by the \"p\" tag MUST be applied for subdomains."
      }
    }
  }
}
```

