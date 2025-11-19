import json
import datetime

def load_questions():
    with open("benchmarks/zap3/zap3_questions.json") as f:
        data = json.load(f)
    return data["questions"]

def run_zap3(model_name="grok4"):
    questions = load_questions()
    results = {
        "model": model_name,
        "date": datetime.date.today().isoformat(),
        "scores": {},
        "total": 0
    }

    print(f"Running ZAP3 on {model_name} – {len(questions)} questions")
    print("Copy-paste each question to the model and paste response here when prompted.\n")

    category_scores = {}
    for q in questions:
        print(f"[{q['id']}] {q['category'].upper()}")
        print(q["question"])
        response = input(">>> Model response: ")
        score = float(input("Human score (0-100): "))
        category_scores.setdefault(q["category"], []).append(score)

    # Average per category
    final = round(sum(sum(scores)/len(scores) for scores in category_scores.values()) / 6, 1)
    results["total"] = final
    with open(f"benchmarks/zap3/results/{model_name}_{datetime.date.today()}.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nZAP3 Complete – Score: {final}/100"
    print(f"Results saved to benchmarks/zap3/results/{model_name}_{datetime.date.today()}.json")

if __name__ == "__main__":
    import sys
    model = sys.argv[1] if len(sys.argv) > 1 else "grok4"
    run_zap3(model)
