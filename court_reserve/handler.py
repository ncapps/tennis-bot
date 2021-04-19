""" Handler for court reserve spider
"""
from os import getenv

from scrapy.crawler import CrawlerProcess
from spider import CourtReserveSpider
from helpers import today_offset
import settings


def main():
    """CLI entry point"""
    reserve_court()


def reserve_court():
    """Run Court Reserve Spider"""
    spider_settings = settings.SETTINGS.copy()
    spider_settings["ORG_ID"] = getenv("ORG_ID")
    spider_settings["USERNAME"] = getenv("USERNAME")
    spider_settings["PASSWORD"] = getenv("PASSWORD")
    spider_settings["RESERVE_DATE"] = today_offset(
        settings.SETTINGS.get("DAY_OFFSET", 0)
    )
    spider_settings["MEMBER_IDS"] = getenv("MEMBER_IDS").split(",")

    process = CrawlerProcess(settings=spider_settings)
    process.crawl(CourtReserveSpider)
    process.start()


if __name__ == "__main__":
    main()
