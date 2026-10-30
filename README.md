# Google Ads API with Python — code from the Marketing Watch House videos

By **Roman Petrochenkov** · [Website](https://rpetrochenkov.co.uk/?utm_source=github&utm_medium=readme&utm_campaign=google_ads_tutorials)
· [LinkedIn](https://www.linkedin.com/in/rpetrochenkov/)
· [YouTube: Marketing Watch House](https://www.youtube.com/channel/UCGVixrs0am6EoF9O16C5lpQ)

The code from my 2020–2021 "Google Ads Automation with Python" videos:

| # | Video |
|---|---|
| 1 | [How to connect to the API](https://www.youtube.com/watch?v=cKODT6-u_bA) |
| 2 | [Running any script](https://www.youtube.com/watch?v=uw8XIVxNoXM) |
| 3 | [How to build reports in the API and Python](https://www.youtube.com/watch?v=ELzngMIgYts) |
| 4 | [Getting a report in pandas and Excel](https://www.youtube.com/watch?v=oe6t4l6NVDE) |

> **Written in 2020** for Google Ads API v5, which has since been sunset, so
> it needs more than a version bump to run today. For current setup and access steps, see the
> [Google Ads API documentation](https://developers.google.com/google-ads/api/docs/start).

## Layout

- `creds_example/googleads.yaml` — template. Copy it to `creds/googleads.yaml` (that folder is gitignored) and
  fill in your own credentials there; never put real values in `creds_example/`.
- `config/config.json` — put your own account ID in place of `INSERT_CUSTOMER_ID` (don't commit that change).
- `src/test_google_ads_access/download_keywords_from_account.py` — the example from the videos.

Something unclear? [Open an issue](https://github.com/RPetrochenkov/google_ads_tutorials/issues/new).
