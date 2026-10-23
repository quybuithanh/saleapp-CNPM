from eapp.models import Category, Product
from eapp import app

def load_categories():
    return Category.query.order_by('id').all()

def load_products(kw=None, cate_id=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))

    if cate_id:
        query = query.filter(Product.category_id==int(cate_id))

    page_size = app.config['PAGE_SIZE']
    start = (page - 1) * page_size #chỉ số trang đầu: page = 1 thì start = (1-1) * 8 = 0
    query = query.slice(start, start + page_size) #giống cắt mảng bắt đầu từ 0 -> 0 + 8 nên chỉ lấy 8 sản phẩm

    return query.all()

def count_products():
    return Product.query.count()