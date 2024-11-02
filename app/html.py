HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Twitter Text Extractor API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            max-width: 1000px;
            margin: 0 auto;
            color: #333;
            font-size: 18px;
        }
        @media (max-width: 768px) {
            body { padding: 10px; }
            pre { font-size: 14px; }
        }
        h1, h2 { color: #2c3e50; }
        pre, code { font-family: 'Courier New', Courier, monospace; background-color: #f8f8f8; border-radius: 8px; }
        pre { padding: 15px; overflow-x: auto; }
        code { padding: 2px 4px; }
        .endpoint { background-color: #e7f2fa; padding: 10px; border-left: 4px solid #3498db; margin-bottom: 20px; border-radius: 9px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        .twitter-link {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #1DA1F2;
            text-decoration: none;
            transition: opacity 0.2s;
            vertical-align: middle;
            line-height: 1;
        }
        .twitter-link:hover {
            opacity: 0.8;
        }
        .twitter-icon {
            width: 20px;
            height: 20px;
            display: inline-block;
            vertical-align: middle;
        }
        .github-link {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: #333;
            text-decoration: none;
            transition: opacity 0.2s;
            vertical-align: middle;
            line-height: 1;
        }
        .github-link:hover {
            opacity: 0.8;
        }
        .github-icon {
            width: 20px;
            height: 20px;
        }
    </style>
</head>
<body>
    <h1>Twitter Text Extractor API</h1>

    <h2>What is this?</h2>
    <p>This is a simple API service that extracts text content from Twitter/X posts. It provides:</p>
    <ul>
        <li>Easy access to tweet content through a simple GET request</li>
        <li>Clean text extraction without requiring Twitter API credentials</li>
        <li>Support for both twitter.com and x.com URLs</li>
        <li>Lightweight and fast response times</li>
    </ul>

    <h2>Implementation</h2>
    <p>This API is built upon the following references:</p>
    <ul>
        <li>Twitter's CDN API: <code>https://cdn.syndication.twimg.com/tweet-result?id=[tweet_id]&token=[token]</code></li>
        <li><a href="https://react-tweet.vercel.app/api/tweet/1849799664125739303">React-Tweet Project</a> - A wrapper for Twitter's CDN API</li>
        <li><a href="https://r.jina.ai/twitter_url">Jina AI API</a> - Supports content retrieval from Twitter and other platforms</li>
        <li>For more details, see this <a href="https://x.com/slippertopia/status/1852523921330893082">reference tweet</a></li>
    </ul>
    <h2>Usage</h2>
    <div class="endpoint">
        <p><strong>URL:</strong> <code>https://xreader.vercel.app/</code></p>
        <p><strong>Endpoint:</strong> <code>/{twitter_url}</code></p>
        <p><strong>Method:</strong> GET</p>
    </div>
    <h2>Example</h2>
    <pre>curl 'https://xreader.vercel.app/https://x.com/EllenDeGeneres/status/440322224407314432'</pre>
    <h2>Response Format</h2>
    <pre>{
    "text": "If only Bradley's arm was longer. Best photo ever. #oscars http://t.co/C9U5NOtGap",
    "status": "success"
}</pre>
    <h2>Error Handling</h2>
    <table>
        <tr>
            <th>Status Code</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>200</td>
            <td>Success</td>
        </tr>
        <tr>
            <td>400</td>
            <td>Invalid URL format</td>
        </tr>
    </table>

    <h2>Source Code</h2>
    <p>This is an open-source project. You can deploy your own instance or contribute to the codebase:
        <a href="https://github.com/ultrasev/xreader" class="github-link">
            <svg class="github-icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
            </svg>
            View on GitHub
        </a>
    </p>

    <h2>Contact</h2>
    <p>For questions or support, reach out on Twitter:
        <a href="https://x.com/slippertopia" class="twitter-link">
            <svg class="twitter-icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
            @slippertopia
        </a>
    </p>
</body>
</html>
"""
