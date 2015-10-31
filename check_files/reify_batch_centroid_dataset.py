from bigml.api import BigML
api = BigML()

source1 = api.create_source("iris.csv")
api.ok(source1)

dataset1 = api.create_dataset(source1)
api.ok(dataset1)

cluster1 = api.create_cluster(dataset1)
api.ok(cluster1)

batchcentroid1 = api.create_batch_centroid(cluster1, dataset1, \
    {'output_dataset': True})
api.ok(batchcentroid1)

dataset2 = api.get_dataset(batchcentroid1['object']['output_dataset_resource'])
api.ok(dataset2)

dataset2 = api.update_dataset(dataset2, \
    {'fields': {u'000000': {'name': u'cluster'}},
     'name': u'my_dataset_from_batch_centroid_name'})
api.ok(dataset2)
