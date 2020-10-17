from src import gads_client, config
from src.models.utils import choose_account_id

import sys
from google.ads.google_ads.errors import GoogleAdsException

# Put an account id to download stats from. Note: not MCC, no dash lines
CUSTOMER_ID = ""


def main(client, customer_id):
    ga_service = client.get_service("GoogleAdsService", version="v5")

    query = """
        SELECT
          campaign.id,
          campaign.name,
          ad_group.id,
          ad_group.name,
          ad_group_criterion.criterion_id,
          ad_group_criterion.keyword.text,
          ad_group_criterion.keyword.match_type,
          metrics.impressions,
          metrics.clicks,
          metrics.cost_micros
        FROM keyword_view
        WHERE
          segments.date DURING LAST_7_DAYS
          AND campaign.advertising_channel_type = 'SEARCH'
          AND ad_group.status = 'ENABLED'
          AND ad_group_criterion.status IN ('ENABLED', 'PAUSED')
        ORDER BY metrics.impressions DESC
        LIMIT 50"""

    # Issues a search request using streaming.
    response = ga_service.search_stream(customer_id, query)
    keyword_match_type_enum = client.get_type(
        "KeywordMatchTypeEnum", version="v5"
    ).KeywordMatchType
    try:
        for batch in response:
            for row in batch.results:
                campaign = row.campaign
                ad_group = row.ad_group
                criterion = row.ad_group_criterion
                metrics = row.metrics
                keyword_match_type = keyword_match_type_enum.Name(
                    criterion.keyword.match_type
                )
                print(
                    f'Keyword text "{criterion.keyword.text}" with '
                    f'match type "{keyword_match_type}" '
                    f"and ID {criterion.criterion_id} in "
                    f'ad group "{ad_group.name}" '
                    f'with ID "{ad_group.id}" '
                    f'in campaign "{campaign.name}" '
                    f"with ID {campaign.id} "
                    f"had {metrics.impressions} impression(s), "
                    f"{metrics.clicks} click(s), and "
                    f"{metrics.cost_micros} cost (in micros) during "
                    "the last 7 days."
                )
    except GoogleAdsException as ex:
        print(
            f'Request with ID "{ex.request_id}" failed with status '
            f'"{ex.error.code().name}" and includes the following errors:'
        )
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f"\t\tOn field: {field_path_element.field_name}")
        sys.exit(1)


if __name__ == "__main__":
    id_to_load = choose_account_id(CUSTOMER_ID, config.get("test_account_id", None))
    main(gads_client, id_to_load)
