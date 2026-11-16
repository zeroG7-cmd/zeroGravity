# operations/office

Data the zeroGravity Office (Zero Command, `/business/`) reads and writes.

| File | What it is | Who edits it |
|---|---|---|
| `readiness.json` | Launch Readiness gates and the check for each item | You, rarely (add your `website_domain` once the site is live) |
| `leads.json` | Leads board | The Office (ADD LEAD form) |
| `plan_judge.json` | Latest AI judge results for the King's Trust plan | The judge (manual on 16 Nov, automatic from build 2) |
| `competitors.json` | Structured competitor data for RESEARCH | You or a research sweep |
| `content_tags.json` | Clip tags (hero / b-roll / reject) | The Office (CONTENT select) |
| `receipts/` | One JSON per cleared READY item: when it passed and on what evidence | The Office, automatically |
| `evidence/` | Certificates and policies, one folder per item id (e.g. `evidence/flyer_id/`) | You. **Gitignored. Never commit it: this repo is public.** |

Rules: nothing in here has a "done" switch. Items clear when their check passes.
