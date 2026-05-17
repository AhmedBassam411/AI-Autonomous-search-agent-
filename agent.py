from backend.graph import build_graph

def main():
    print("🧠 AI Research Agent (No FastAPI)")
    print("-" * 40)

    graph = build_graph()

    while True:
        query = input("\nEnter topic (or 'exit'): ")

        if query.lower() == "exit":
            break

        try:
            result = graph.invoke({"input": query})

            print("\n📌 PLAN")
            print(result.get("plan", ""))

            print("\n🔍 ANALYSIS")
            print(result.get("analysis", ""))

            print("\n📄 REPORT")
            print(result.get("report", ""))

        except Exception as e:
            print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    main()