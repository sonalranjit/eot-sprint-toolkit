import warc

f = warc.open("/Users/sonal/SideProjects/WarcCreator/test_data/crlf_at_1k_boundary.warc.gz")

for record in f:
    print record['WARC-Target-URI'], record['Content-Length']