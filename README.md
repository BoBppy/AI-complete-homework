# 文档AI助手

这是一个基于Python的Web应用程序，可以帮助用户使用AI来扩充和优化Word文档内容。

## 功能特点

- 支持上传Word文档（.docx格式）
- 使用OpenAI API进行文档内容分析和扩充
- 支持自定义API端点
- 提供思维链（Chain of Thought）分析过程
- 实时显示处理进度和日志
- 支持文件拖放上传
- 现代化的用户界面

## 安装要求

1. Python 3.7+
2. OpenAI API密钥

## 安装步骤

1. 克隆仓库：
```bash
git clone [repository-url]
cd [repository-name]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python main.py
```

应用将在 http://localhost:8000 启动

## 使用说明

1. 打开浏览器访问 http://localhost:8000
2. 输入您的OpenAI API密钥
3. 上传Word文档或将文档拖放到上传区域
4. 在提示词输入框中输入额外的处理要求（可选）
5. 等待AI处理完成
6. 下载处理后的文档

## 注意事项

- 请确保您有有效的OpenAI API密钥
- 目前仅支持.docx格式的文档
- 处理时间取决于文档大小和API响应速度

## 许可证

MIT License 