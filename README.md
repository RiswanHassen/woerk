# WOERK

**AI-Powered Job Application Tooling**

WOERK generates structured, targeted job application materials using LLM-based text generation. It produces cover letters, CV adaptations, and application narratives tailored to specific job postings — without resorting to generic template fill-in.

---

## Approach

Most AI-assisted application tools paste your CV into a prompt and call it done. WOERK takes a different approach:

- **Structured generation** — decomposes the application into components (qualification mapping, motivation narrative, cultural fit signals) and generates each with appropriate context
- **Job posting analysis** — extracts requirements, implicit expectations, and company signals from the posting itself
- **Consistency checks** — ensures generated materials don't contradict each other or the source CV

## Usage

```bash
python woerk.py --cv path/to/cv.pdf --posting path/to/job.txt --output ./application/
```

## Status

Working prototype. Under active refinement.

## License

See [LICENSE](LICENSE) for details.
