def get_model_text(llm_response: LlmResponse) -> str:
    """Get text from the model response."""

    if (
        llm_response is None
        or llm_response.content is None
        or not llm_response.content.parts
    ):
        return ""

    return llm_response.content.parts[0].text or ""


def after_model_guardrail_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse
) -> GuardrailResult:
    """Track consecutive out-of-scope requests."""

    model_output = get_model_text(llm_response).lower().strip()

    oos_indicators = [
        "outside of my scope",
        "outside of what i can help",
        "outside of my expertise",
        "my focus is on fashion",
        "fashion-related inquiries",
        "fashion-related topics",
        "fashion-related services",
        "only assist with fashion",
        "only help with fashion",
    ]

    is_out_of_scope = any(
        phrase in model_output
        for phrase in oos_indicators
    )

    count = int(
        callback_context.variables.get("out_of_scope_count", 0)
    )

    if is_out_of_scope:
        count += 1
    else:
        count = 0

    callback_context.variables["out_of_scope_count"] = count

    if is_out_of_scope and count >= 3:
        return create_guardrail_result(
            decision="TRIGGER",
            reason="Three consecutive out-of-scope requests detected."
        )

    return create_guardrail_result(
        decision="OK",
        reason=f"Consecutive out-of-scope count: {count}"
    )