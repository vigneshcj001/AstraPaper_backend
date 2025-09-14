from app.services.ollama_service import run_ollama
async def fuse_responses(question: str, text:str)->str:
    qwen_out = await run_ollama("qwen3:4b",f"Answer based on:\n{text}\nQuestion:{question}")
    deepseek_out = await run_ollama("deepseek-r1:1.5b", f"Critically review this answer: {qwen_out} and improve it if necessary.")
    return f"Qwen3 Response: {qwen_out}\nDeepSeek Critique: {deepseek_out}"