from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from transformers import pipeline

# Load the GPT-2 model for text generation
chatbot_model = pipeline("text-generation", model="gpt2")

def ai_get_response(user_message):
    """
    Function to send the user message to GPT-2 and get a generated response.
    """
    # response = chatbot_model(user_message, max_length=50, num_return_sequences=1)
    # return response[0]['generated_text']

    placement_context = (
        "You are an assistant specialized in college placements. "
        "Answer the following question related to college placements: "
    )

    # Combine the context with the user message
    input_message = placement_context + user_message

    # Get the AI-generated response from GPT-2
    response = chatbot_model(input_message, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

def chatbot_response(request):
    """
    Django view to process the user's message and return the AI chatbot's response.
    """
    user_message = request.GET.get('message', '')

    if not user_message:
        return JsonResponse({'response': "Please enter a message."})

    response = ai_get_response(user_message)
    return JsonResponse({'response': response})

def chatbot_view(request):
    """
    View to render the chatbot HTML page.
    """
    return render(request, 'chatbot.html')