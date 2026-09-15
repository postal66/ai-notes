<!-- social-ops-fingerprint:1118d0cdeeb10ede0b398e23da3d81244e4c975dd51cd4aea7b69902901562a8 -->
---
title: What Kind of Files does Claude Allow Me to Upload
---
# What Kind of Files does Claude Allow Me to Upload

![What Kind of Files does Claude Allow Me to Upload](https://resource.cometapi.com/blog/uploads/2025/06/What-Kind-of-Files-does-Claude-Allow-Me-to-Upload.webp)

Claude, Anthropic’s conversational AI, offers a rich set of file‑upload capabilities—both in its web interface and via its API—that let you work seamlessly with documents, images, datasets, code files and more. Understanding exactly what you can upload, how to manage those files, and how to integrate them into your workflows allows you to reduce repetitive uploads, share resources across projects, and leverage Claude’s advanced reasoning on diverse content types. Below, we explore, in depth, the various file formats and methods Claude supports, structured with clear questions as secondary headings and detailed subsections beneath each.

## What document types does Claude support?

### Supported Document Formats

Claude can ingest and analyze a wide range of common document types directly in the chat or within a project knowledge base. These include:

- **PDF** (`.pdf`)
- **Word Documents** (`.docx`)
- **Plain Text** (`.txt`)
- **Rich Text** (`.rtf`)
- **OpenDocument Text** (`.odt`)
- **HTML** (`.html`)
- **EPUB** (`.epub`)
- **JSON** (`.json`)

> **Tip:** While you can upload CSVs (`.csv`) anywhere, Excel workbooks (`.xlsx`) require that you have the Analysis Tool enabled in your account or project.

### Upload Limits and Constraints

- **Maximum file size:** 30 MB per file
- **Maximum files per chat session:** 20 files
- **Knowledge base storage:** Unlimited files, subject to overall context‑window limits

### Typical Use Cases

- **Legal & Contract Review:** Upload multi‑hundred‑page PDF contracts for clause‑by‑clause summarization.
- **Market Research Reports:** Bundle dozens of PDF or Word research studies for side‑by‑side comparison.
- **Academic Literature Surveys:** Import multiple articles at once to generate a cohesive literature review.

## Which image formats does Claude support?

### Supported Image Types

Claude accepts the following image formats for visual question‑answering and analysis:

- **JPEG** (`.jpg`, `.jpeg`)
- **PNG** (`.png`)
- **GIF** (`.gif`)
- **WEBP** (`.webp`)

Images may be up to 30 MB in size and up to 8,000 × 8,000 pixels in resolution. For optimal detail, aim for at least 1,000 × 1,000 pixels.

### Image Upload Use Cases

- **Visual Q&A:** Upload product photos, diagrams, or maps and ask Claude to identify objects, explain layouts, or locate points of interest.
- **Chart & Graph Interpretation:** Share a bar chart, scatterplot or pie chart for Claude to extract key data insights.
- **Design Feedback:** Get instant creative direction on marketing assets—ad banners, social‑media graphics, slide decks and more.

## How can you upload a PDF via the API?

### 1. Direct URL Reference

If your PDF is publicly hosted, the simplest approach is to provide its URL in your API call. Claude will fetch and parse it automatically:

```
{
  "type": "document",
  "source": {
    "type": "url",
    "url": "https://example.com/annual-report.pdf"
  }
}
```

### 2. Base64‑Encoded Content

When public hosting isn’t possible, you can embed the PDF directly as a Base64 string. While more flexible, each request must include the full encoded data:

```
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": "<BASE64_ENCODED_PDF>"
  }
}
```

### 3. Files API for Bulk Management

To avoid repeatedly uploading the same large file, use Claude’s Files API (in Beta since April 14, 2025) to store it once and reference it by `file_id` thereafter.

#### a. Uploading the File

```
curl -X POST https://api.anthropic.com/v1/files \
  -H "x-api-key: $API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -F "file=@/path/to/annual-report.pdf"
```

#### b. Referencing in a Chat or Code Call

```
{
  "type": "document",
  "source": {
    "type": "file",
    "file_id": "file_ABC123xyz"
  }
}
```

### File Type Mapping in the Files API

| File Extension | MIME Type | Content Category |
| --- | --- | --- |
| .pdf | application/pdf | document |
| .txt | text/plain | document |
| .jpg/.png | image/jpeg, image/png | image |
| .csv | text/csv | container\_upload |

## How do you upload spreadsheets and datasets?

### CSV vs. Excel (XLSX)

- **CSV (`.csv`):** Instantly supported—just drag and drop into chat or your project.
- **Excel (`.xlsx`):** Requires the Analysis Tool; once enabled, you can upload and perform deep table analysis.

### Large‑File Support Update

As of December 19, 2024, Claude’s web and mobile apps support analyzing Excel workbooks up to 30 MB in size—perfect for enterprise‑scale financial models or pooled research datasets.

### Common Data‑Driven Workflows

- **Financial Audits:** Upload your entire budget workbook and run variance checks automatically.
- **Scientific Research:** Import raw experiment logs, calculate statistical summaries, and visualize distributions.
- **Sales Trend Forecasting:** Combine multiple quarterly spreadsheets to generate multi‑year sales projections.

## How does the Files API simplify file management?

### One‑Time Upload, Unlimited Reuse

Once uploaded, files live in your workspace and can be referenced by any chat or code request:

- **List all files:** `GET /v1/files`
- **Fetch metadata:** `GET /v1/files/{file_id}`
- **Delete a file:** `DELETE /v1/files/{file_id}`

### Storage Limits & Policies

- **Max per file:** 32 MB
- **Total workspace storage:** 100 GB
- **Retention:** Files persist until explicitly deleted.
- **Download:** Only output files generated by Claude’s code tool can be downloaded; originals remain view‑only.

### Cost Structure

- **File operations:** Free (upload, list, delete, metadata).
- **Processing fees:** Standard input‑token billing applies when Claude reads your file in a chat or analysis request.

## How can you leverage the code execution tool to enhance your workflows?

### Supported Data Formats for Code

When you need custom analysis—beyond built‑in table queries—Claude’s Python sandbox can load CSVs, Excel workbooks, JSON datasets, and more directly from your Files API storage.

### Typical Code‑Driven Process

1. **Upload data file** via Files API (e.g., `file_data123.csv`).
2. **Invoke code execution** in chat: `{ "type": "code_execution", "source": { "type": "file", "file_id": "file_data123" } }`
3. **Receive plots or script outputs** back in the conversation, or download generated artifacts (charts, transformed CSVs).

### Security and Compliance

- **Private Storage:** Only your workspace’s API keys can access the files.
- **Encrypted at Rest & In Transit:** All uploads and storage are encrypted end‑to‑end.
- **Access Controls:** Manage and rotate API keys via the Anthropic dashboard.

## What limitations and best practices should you consider?

While Claude’s file upload features are highly capable, certain limits and considerations ensure optimal performance and cost efficiency.

### Size and Quantity Limits

- **Chat uploads:** Maximum 30 MB per file, up to 20 files per chat.
- **Project knowledge bases:** Also 30 MB per file, unlimited files, but total extracted content must fit within Claude’s context window.

### Model Compatibility

- **Document support:** PDF uploads require Claude 3.5 Sonnet or newer for full visual analysis. Models older than Sonnet 3.5 will only extract text from PDFs over 100 pages or when used in a knowledge base.
- **Image and general file support:** Available in all Claude 3+ models; code and data formats require Claude 3.5 Haiku or Claude 3.7+ for code execution.

## Getting Started

CometAPI provides a unified REST interface that aggregates hundreds of AI models—including Claude family—under a consistent endpoint, with built-in API-key management, usage quotas, and billing dashboards. Instead of juggling multiple vendor URLs and credentials.

Developers can access [Claude Sonnet 4 API](https://www.cometapi.com/claude-sonnet-4-api/)  (model: `claude-sonnet-4-20250514` ; `claude-sonnet-4-20250514-thinking`) and [Claude Opus 4 API](https://www.cometapi.com/claude-opus-4-api/) (model: `claude-opus-4-20250514`; `claude-opus-4-20250514-thinking`)etc through [CometAPI](https://www.cometapi.com/).  . To begin, explore the model’s capabilities in the [Playground](https://www.cometapi.com/console/playground) and consult the [API guide](https://apidoc.cometapi.com/) for detailed instructions. Before accessing, please make sure you have logged in to CometAPI and obtained the API key. CometAPI’ve also added `cometapi-sonnet-4-20250514`and`cometapi-sonnet-4-20250514-thinking` specifically for use in Cursor.

Using Claude model on cometapi has the following advantages:

- Bypass direct Claude file upload limitation issue.
- Easily switch between different AI models if needed

*New to CometAPI?* [Start a free 1$ trial](https://www.cometapi.com/console/login) and unleash Sonnet 4 on your toughest tasks.

We can’t wait to see what you build. If something feels off, hit the feedback button—telling us what broke is the fastest way to make it better.

## Conclusion

By supporting a broad array of file types—from multi‑page PDFs and Word documents to high‑resolution images, CSVs and Excel workbooks—it provides a true one‑stop data processing hub. The addition of the Files API Beta (April 2025) and the extension of large‑file support for spreadsheets (December 2024) empower both enterprise and academic users to centralize, streamline, and scale their workflows. Whether you need to summarize legal contracts, extract insights from market data, interpret complex visuals, or run custom analyses in Python, mastering Claude’s file‑upload and management features is key to unleashing its full AI‑driven potential.

---

*Originally published at [https://www.cometapi.com/what-kind-of-files-does-claude-allow-me-to-upload/](https://www.cometapi.com/what-kind-of-files-does-claude-allow-me-to-upload/).*
