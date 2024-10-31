ITEM_PIPELINES = {
   'phongtro.pipelines.CSVDBPhongTroPipeline': 100,
   'phongtro.pipelines.JsonDBPhongTroPipeline': 200,
   'phongtro.pipelines.MongoDBPhongTroPipeline': 300,
}
SPIDER_MODULES = ['phongtro.spiders']
NEWSPIDER_MODULE = 'phongtro.spiders'