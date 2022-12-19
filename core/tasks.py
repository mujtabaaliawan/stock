from category.models import Category
from company.models import Company
from stock_detail.models import StockDetail
from stock_detail.serializers import StockDetailSerializer
from favourite.tasks import mail_favourite


def dataupdate(market_data):

    StockDetail.objects.filter(is_latest=True).update(is_latest=False)

    for company_data in market_data:
        category, created = Category.objects.get_or_create(name=company_data['category'])
        company, created = Company.objects.get_or_create(name=company_data['company'],
                                                         defaults={'category_id': category.id})
        company_data['company_id'] = company.id
        company_data['category_id'] = category.id
        company_data['is_latest'] = True

        serializer = StockDetailSerializer(data=company_data)
        serializer.is_valid()
        serializer.save()

    mail_favourite()

