# flask-init-directory-structure

一个即可 `flask run` 又可 `python3 app.py` 运行的目录结构。

## config

通过判断当前是否为调试模式去返回配置。

注意：

`app.py` 中默认设置开启了调试模式，但因为是加载配置之后再开启的调试模式，因为返回的还是 `prod`配置。 因此若想返回 `dev` 配置则需要添加环境变量。

```bash
export FLASK_DEBUG=1
```

## 参考

1. [Structure of a Flask Project](https://lepture.com/en/2018/structure-of-a-flask-project) -> [译文](https://www.jianshu.com/p/49dc66141d20)
2. [第 125 天：Flask 项目结构](https://developer.aliyun.com/article/866859)

---

...待完善。
