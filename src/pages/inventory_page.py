from utils.config import INVENTORY_URL


class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_list = page.locator(".inventory_list")

    def is_opened(self) -> bool:
        return (
            self.page.url == INVENTORY_URL and
            self.inventory_list.is_visible()
        )