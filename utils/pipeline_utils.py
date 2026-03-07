from pprint import pprint # function to make the output of various pipelines a little more user friendly!

def pretty_print_pipeline_result(result):
    if isinstance(result, dict):
        if "labels" in result and "scores" in result:
            print("Top labels:")
            for label, score in zip(result["labels"], result["scores"]):
                print(f"- {label}: {score:.3f}")
            return
        if "answer" in result and "score" in result:
            print(f"Answer: {result['answer']}")
            print(f"Score: {result['score']:.3f}")
            if "start" in result and "end" in result:
                print(f"Span: {result['start']} to {result['end']}")
            return
        pprint(result, sort_dicts=False)
        return

    if isinstance(result, list):
        if all(isinstance(item, dict) and {"entity", "word", "score"}.issubset(item.keys()) for item in result):
            print("Named entities:")
            for item in result:
                word = item.get("word", "")
                entity = item.get("entity", "")
                score = item.get("score", 0.0)
                print(f"- {word} ({entity}, score={score:.3f})")
            return

        if all(isinstance(item, dict) and {"label", "score"}.issubset(item.keys()) for item in result):
            print("Predictions:")
            for item in result:
                print(f"- {item['label']}: {item['score']:.3f}")
            return

        if all(isinstance(item, dict) and "generated_text" in item for item in result):
            print("Generated text:")
            for i, item in enumerate(result, start=1):
                print(f"[{i}] {item['generated_text']}")
            return

        if all(isinstance(item, dict) and "sequence" in item for item in result):
            print("Mask suggestions:")
            for i, item in enumerate(result, start=1):
                token_str = item.get("token_str", "").strip()
                score = item.get("score", 0.0)
                print(f"[{i}] {token_str} (score={score:.3f})")
                print(f"    {item.get('sequence', '')}")
            return

        pprint(result, sort_dicts=False)
        return

    print(result)