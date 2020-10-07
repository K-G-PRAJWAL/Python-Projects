import bs4
import requests

# Check price of a product on Snapdeal


def getPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('html body div#content_wrapper section#overviewBlk.pdp-section.clearfix div#productOverview.product-detail.clearfix.col-xs-24.reset-padding.favDp div.col-xs-14.right-card-zoom.reset-padding div.pdp-comp.comp-product-description.clearfix div.pdp-fash-topcenter-inner.layout div.container-fluid.reset-padding div#buyPriceBox.fashionPriceTile.row div.row.reset-margin div.col-xs-14.reset-padding.padL8 div.disp-table div.pdp-e-i-PAY-r.disp-table-cell.lfloat span.pdp-final-price')
    return elems[0].text.strip()


price = getPrice(
    'https://www.snapdeal.com/product/veirdo-100-percent-cotton-multi/633668842498#bcrumbLabelId:17')
print(price)
price2 = getPrice(
    'https://www.snapdeal.com/product/surt-cotton-blend-blue-shirt/633090512655')
print(price2)
