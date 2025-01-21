from blogs.models import BlogKatalogModel,BlogMaxsulotModel

def run():
    kat1 = BlogKatalogModel.objects.create(title = 'Elektronika',status = 'Faol')
    kat2 = BlogKatalogModel.objects.create(title = 'Maishiy texnika',status = 'Faol')
    kat3 = BlogKatalogModel.objects.create(title = 'xojalik mollari',status = 'Faol')

    BlogMaxsulotModel.objects.bulk_create([
        BlogMaxsulotModel(name = 'Telefon', narx = 1100000,kategorya=kat1,ombor = True),
        BlogMaxsulotModel(name = 'UN',narx = 11200,kategorya = kat3,ombor = True),
        BlogMaxsulotModel(name = 'Tifal',narx = 67000,kategorya = kat2,ombor=False),
    ])



