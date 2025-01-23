# Qwen 2.5-7B Chat Interface

Running Qwen 2.5-7B Chat Interface locally. Check this website for more information: https://qwen.readthedocs.io/en/latest/run_locally/mlx-lm.html


# Install Qwen locally

```bash
uv sync
```

```bash
uv run mlx_lm.convert --hf-path Qwen/Qwen2.5-7B-Instruct --mlx-path mlx/Qwen2.5-7B-Instruct/ -q
```

 
```bash
uv run llm.py
```
