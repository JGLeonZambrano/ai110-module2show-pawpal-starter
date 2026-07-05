# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Used Claude (claude.ai) as AI coding assistant for system design review, implementing scheduling algorithms, debugging, and adding stretch features including tabulate formatting and JSON persistence.

**What did the agent do?**

- Reviewed the UML class design structure
- Suggested and explained lambda functions for sorting
- Generated pytest test cases for edge cases
- Implemented save_to_json/load_from_json methods
- Suggested tabulate formatting for CLI output

**What did you have to verify or fix manually?**

- Removed incorrect `tasks` parameter from Pet.__init__
- Fixed `mark_complete()` which incorrectly took a `task` parameter
- Changed `self.description = []` to `self.description = description`
- Kept dictionary-based priority sorting over AI's list suggestion
- Fixed period instead of comma in Task.__init__ signature
- Changed some naming conventions to elements that were easier to understand

