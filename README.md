<img src="public/logo.png" alt="logo" width="200"/>

# Twitter 文本提取 API

一个简单的 API 项目，用于提取 Twitter/X 平台帖子的文本内容，可部署在 Vercel 或者 VPS 上。

## 有哪些功能？

- 通过简单的 GET 请求轻松访问推文内容
- 无需 Twitter API 凭证即可清洗提取文本
- 同时支持 twitter.com 和 x.com 的 URL
- 轻量级设计，响应速度快

## 实现原理

本 API 封闭了以下接口：

- Twitter 的 CDN API：`https://cdn.syndication.twimg.com/tweet-result?id=[tweet_id]&token=[token]`
- [React-Tweet 项目](https://react-tweet.vercel.app/) - Twitter CDN API 的封装
- [Jina AI API](https://r.jina.ai/) - 支持从 Twitter 等平台获取内容
- 更多详情请参考[这条推文](https://x.com/slippertopia/status/1852523921330893082)

### 为什么需要 Jina AI API？

对于长推文，CDN API 返回的数据是截断的，这种情况下，本 API 会调用 Jina AI API 进行再次提取。

## 使用方法

### API 接口

- **URL**: [`https://xreader.vercel.app/x`](https://xreader.vercel.app/x)
- **查询参数**: `url` - Twitter/X 帖子的 URL
- **请求方式**: GET

### 示例

```bash
curl 'https://xreader.vercel.app/x?url=https://x.com/EllenDeGeneres/status/440322224407314432'
```

### 返回格式

```json
{
  "text": "If only Bradley's arm was longer. Best photo ever. #oscars http://t.co/C9U5NOtGap",
  "status": "success"
}
```

### 错误处理

| 状态码 | 说明         |
| ------ | ------------ |
| 200    | 成功         |
| 400    | URL 格式无效 |
| 500    | 服务器错误   |

## Vercel 部署

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fultrasev%2Fxreader)

## 联系方式

如有问题或需要支持，请通过 Twitter 联系：[@slippertopia](https://x.com/slippertopia)
