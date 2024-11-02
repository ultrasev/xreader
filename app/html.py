HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Twitter Text GET API</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 1000px; margin: 0 auto; color: #333; }
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
    </style>
</head>
<body>
    <h1>Twitter Text GET API</h1>
    <h2>Usage</h2>
    <div class="endpoint">
        <p><strong>Endpoint:</strong> <code>/{twitter_url}</code></p>
        <p><strong>Method:</strong> GET</p>
    </div>
    <h2>Example</h2>
    <pre>curl 'https://your-domain.com/https://x.com/EllenDeGeneres/status/440322224407314432'</pre>
    <h2>Response Format</h2>
    <pre>{
    "text": "Tweet content",
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
</body>
</html>
"""
