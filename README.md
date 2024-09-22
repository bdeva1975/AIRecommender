# AIRecommender

AIRecommender is a smart AI service matcher using OpenAI's GPT models. This tool analyzes user requirements and suggests relevant AI services, providing personalized recommendations with justifications.

## Overview

AIRecommender uses a Retrieval-Augmented Generation approach to match user queries with the most relevant AI services. It combines the power of vector databases for efficient searching with the natural language understanding capabilities of large language models to create personalized summaries and recommendations.

## Architecture

1. **Data Preparation**: AI service descriptions are chunked and converted into vectors using OpenAI's embedding model. These vectors are then stored in a local Chroma database.

2. **User Query**: The user submits a request describing their AI service needs.

3. **Vector Matching**: The user's query is converted to a vector and matched against the stored vectors in the Chroma database.

4. **Personalized Recommendation**: The matched service descriptions and the user's query are passed to OpenAI's GPT model to generate personalized recommendations and summaries.

## Use Cases

- Creating personalized AI service recommendations with justifications.
- Generating custom "Top AI Tools" lists for specific domains or applications.
- Helping developers and businesses find the right AI tools for their projects.

## Components

1. `recommendations_lib.py`: The backend library that handles interactions with OpenAI's API and the Chroma database.
2. `recommendations_app.py`: The Streamlit frontend for user interaction.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/bdeva1975/AIRecommender.git
   cd AIRecommender
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your_api_key_here`

4. Prepare the vector database:
   ```
   python populate_collection.py
   ```

5. Run the Streamlit app:
   ```
   streamlit run recommendations_app.py
   ```

## Usage

1. Open the Streamlit app in your browser (typically at `http://localhost:8501`).
2. Enter your AI service requirements in the text input.
3. Click "Get Recommendations" to receive personalized AI service suggestions.

## Future Improvements

- Integrate with persistent data stores for scalability.
- Implement user feedback mechanisms to improve recommendations over time.
- Add support for more AI service providers and regular updates to the service database.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
