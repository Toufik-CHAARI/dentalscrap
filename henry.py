import requests

url = "https://www.henryschein.fr/webservices/JSONRequestHandler.ashx"

payload = "ItemArray=%257B%2522ItemDataToPrice%2522%253A%255B%257B%2522ProductId%2522%253A%2522951-7294%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522886-4076%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522886-4074%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522886-4075%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522886-4073%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-2611%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-8738%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-8739%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522890-5353%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522890-5354%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-8740%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-8741%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522952-1261%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522952-1263%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522892-7783%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-8736%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522891-8737%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%252C%257B%2522ProductId%2522%253A%2522883-8023%2522%252C%2522Qty%2522%253A%25221%2522%252C%2522Uom%2522%253A%2522UN%2522%252C%2522PromoCode%2522%253A%2522%2522%252C%2522CatalogName%2522%253A%2522GENCABI%2522%252C%2522ForceUpdateInventoryStatus%2522%253Afalse%252C%2522AvailabilityCode%2522%253A%252208%2522%257D%255D%257D&searchType=6&did=dental&catalogName=GENCABI&endecaCatalogName=GENCABI&culture=fr-fr"
headers = {
    "cookie": "HSCSProfileNonHttpOnly=PreferredCultureId%3Dfr-FR; HSCSProfile=HSCSProfile%3D%257ba8494954-a4dc-4099-b86d-dc882e0e0b8c%257d%26ExchangeMessage%3D; OneWebSessionCookie=AccordianMenuActiveIndex%3D0%26GetNextCounter%3D480%26BrowseSupply_ContShoppingKey%3D%252ffr-fr%252fSearch.aspx%253fsearchkeyWord%253dkavo%252cN%253d4294858868; CampaignHistory=3283%2C3281%2C3257%2C3266%2C3279%2C3225; bm_sv=88F710D3E7C5468E12816047B91D942F~0m8hNiznRfi3gAr%2BCvWuiSu%2B0hhY8CIjWuYrkAiklitlOx2KVzylsKTqcN%2FViEUtrtfkm5%2FFtfIV2qO%2FUOmhuoi%2BfaVRTsOTVwPmZv8r%2BJgdytk2eB%2FNMC2K%2FvPh29OvWSpL9WuFVbt1c4UtAohSH3AaJarN1oMuaAzx0YmLESc%3D",
    "authority": "www.henryschein.fr",
    "pragma": "no-cache",
    "cache-control": "no-cache",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "x-requested-with": "XMLHttpRequest",
    "origin": "https://www.henryschein.fr",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)