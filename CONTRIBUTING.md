# 🤝 Contributing Guidelines

Thank you for your interest in contributing to MultiAgent CrewAI! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Code Standards](#code-standards)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)
- [Questions or Need Help?](#questions-or-need-help)

## Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to:

- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on constructive criticism
- Report inappropriate behavior to maintainers

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git installed
- GitHub account
- Groq API key (for testing)

### Fork and Clone

1. **Fork the repository** on GitHub
   - Click the "Fork" button on the [repository page](https://github.com/Nuthan-hue/MultiAgent_CrewAI)

2. **Clone your fork** locally

```bash
git clone https://github.com/YOUR_USERNAME/MultiAgent_CrewAI.git
cd MultiAgent_CrewAI
```

3. **Add upstream remote** to track original repository

```bash
git remote add upstream https://github.com/Nuthan-hue/MultiAgent_CrewAI.git
git remote -v  # Verify both origin and upstream
```

### Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install development tools
pip install pytest black flake8 isort
```

## Development Workflow

### 1. Create a Feature Branch

Always create a new branch for your work:

```bash
# Update your main branch first
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
# or for bug fixes
git checkout -b fix/bug-description
```

**Branch naming conventions:**
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test improvements

### 2. Make Your Changes

Edit files and make improvements. Follow the [Code Standards](#code-standards) section.

### 3. Test Your Changes

```bash
# Run the application
python main.py

# Run linting
flake8 .
black --check .

# Run any existing tests
pytest
```

### 4. Commit Changes

```bash
# Stage your changes
git add .

# Commit with clear message
git commit -m "feat: Add support for custom agents

- Implement Agent factory pattern
- Add documentation for extending agents
- Include example custom agent implementation"
```

**Commit message format:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Testing
- `chore:` - Maintenance

## Making Changes

### Code Changes

#### Before Making Changes

1. **Discuss large changes**: Open an issue first to discuss major changes
2. **Check existing issues**: Your idea might already be discussed
3. **Review recent commits**: Understand the current direction

#### Guidelines

**Python Code Style:**
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

**Example:**
```python
def search_ai_trends(query: str, num_results: int = 3) -> List[str]:
    """
    Search for AI trends related to the given query.
    
    Args:
        query: Search query for AI trends
        num_results: Number of results to return (default: 3)
    
    Returns:
        List of trend descriptions
    """
    search_tool = WebSearchTool()
    results = search_tool._run(query)
    return results[:num_results]
```

**Comments and Documentation:**
- Comment "why", not "what" the code does
- Update docstrings when changing function behavior
- Add type hints to function parameters

### Documentation Changes

- Use clear, simple language
- Add code examples where helpful
- Keep formatting consistent
- Update table of contents for long documents

### Adding New Agents

1. **Create agent in main.py** with clear role and goal
2. **Add documentation** in ARCHITECTURE.md
3. **Create associated task** with expected output
4. **Update README** with new agent description
5. **Add tests** if applicable

Example:
```python
# In main.py
quality_analyst = Agent(
    role='Quality Analyst',
    goal='Ensure content meets quality standards',
    backstory='You have expertise in quality assurance...',
    verbose=True,
    allow_delegation=False,
    tools=[validation_tool],
    llm=llm
)

# Add to ARCHITECTURE.md
# Create pull request with clear description
```

### Adding New Tools

1. **Implement as BaseTool subclass**
2. **Add comprehensive docstring**
3. **Test the tool independently**
4. **Update documentation** with tool description
5. **Add example usage** in comments

## Submitting Changes

### Before Submitting

- ✅ Test your changes thoroughly
- ✅ Update documentation
- ✅ Follow code standards
- ✅ Check for conflicts with upstream
- ✅ Verify all commits have clear messages

### Create a Pull Request

1. **Push to your fork**

```bash
git push origin feature/your-feature-name
```

2. **Create Pull Request on GitHub**
   - Go to [original repository](https://github.com/Nuthan-hue/MultiAgent_CrewAI)
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Fixes #(issue number)

## Testing Done
How was this tested?

## Screenshots
(if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally
```

3. **Respond to Review Comments**
   - Be open to feedback
   - Make requested changes in new commits
   - Push changes to update PR
   - Explain disagreements respectfully

### Merge Process

After approval:
- Maintainer merges PR
- Your branch is deleted
- Your contribution is published!

## Code Standards

### Python Style

Use **Black** for formatting:

```bash
black .
```

Use **flake8** for linting:

```bash
flake8 .
```

Use **isort** for imports:

```bash
isort .
```

### Pre-commit Checks

Create `.git/hooks/pre-commit` to auto-format before commits:

```bash
#!/bin/sh
black .
isort .
flake8 .
```

### Type Hints

Add type hints to all functions:

```python
def process_data(items: List[str], count: int) -> Dict[str, Any]:
    """Process data items."""
    pass
```

### Docstring Format

Use Google-style docstrings:

```python
def create_agent(role: str, goal: str) -> Agent:
    """
    Create a new CrewAI agent with specified role.
    
    Args:
        role: The role/title of the agent
        goal: The primary goal/objective
    
    Returns:
        An Agent instance ready to execute tasks
        
    Raises:
        ValueError: If role or goal is empty
        
    Example:
        >>> agent = create_agent("Researcher", "Find trends")
        >>> print(agent.role)
        Researcher
    """
    pass
```

## Reporting Issues

### Bug Reports

Use the bug report template:

1. **Go to Issues** → **New Issue**
2. **Title**: Clear, concise description
3. **Description**:
   - Expected behavior
   - Actual behavior
   - Steps to reproduce
   - Environment (OS, Python version)
   - Error message/logs

**Example:**
```
Title: Web search tool fails with special characters

Description:
- Expected: Search works with any query
- Actual: Tool crashes when query contains "&" symbol
- Steps: Run with query "AI & ML trends"
- Error: UnicodeEncodeError...
```

### Bug Report Checklist

- [ ] Descriptive title
- [ ] Clear reproduction steps
- [ ] Expected vs actual behavior
- [ ] Environment details
- [ ] Error logs/screenshots
- [ ] Related issues linked

## Feature Requests

### Requesting Features

1. **Check existing issues** - Feature might be planned
2. **Create new issue** with template:
   - Description of feature
   - Use case and benefit
   - Example behavior
   - Any relevant code

**Example:**
```
Title: Add support for scheduling agent tasks

Description:
Allow agents to schedule tasks to run at specific times, enabling:
- Time-based research refreshes
- Scheduled blog post generation
- Automated content updates

Use case: Generate trending AI news blog post every Sunday at 9 AM

Example:
task.schedule(
    time="09:00",
    frequency="weekly",
    day="sunday"
)
```

### Feature Request Checklist

- [ ] Clear title and description
- [ ] Use case explained
- [ ] Example implementation (optional)
- [ ] No duplicate requests

## Questions or Need Help?

### Getting Answers

1. **Check documentation**
   - [README.md](README.md)
   - [SETUP.md](SETUP.md)
   - [ARCHITECTURE.md](ARCHITECTURE.md)

2. **Search existing issues** - Your question might be answered

3. **Open a discussion** on GitHub Discussions (if available)

4. **Create an issue** with `question` label

### Ask on Issues

```
Title: How to add custom tool to agent?

Question: I want to create a custom tool for my agent. 
Can someone provide guidance on the tool structure and integration?
```

## Recognition

Contributors will be recognized:
- 🌟 In the README contributors section
- 🎉 Special mention for significant contributions
- 📢 Featured in release notes for major features

---

## Summary

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes following standards
4. **Commit** with clear messages
5. **Push** to your fork
6. **Create** a Pull Request
7. **Respond** to review feedback
8. **Merge** and celebrate! 🎉

Thank you for contributing! Your efforts help make this project better for everyone.

**Questions?** Feel free to open an issue!

