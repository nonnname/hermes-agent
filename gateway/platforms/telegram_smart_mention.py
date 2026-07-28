"""Backward-compatible imports for the platform-neutral Smart Mention helpers."""

from gateway.platforms.smart_mention import (
    DEFAULT_MATTERMOST_SMART_MENTION_SYSTEM_PROMPT,
    DEFAULT_SMART_MENTION_SYSTEM_PROMPT,
    SmartMentionClassification,
    SmartMentionConfig,
    build_smart_mention_messages,
    default_smart_mention_system_prompt,
    format_recent_context_for_agent,
    normalize_smart_mention_config,
    parse_smart_mention_response,
    truncate_text,
)

__all__ = [
    "DEFAULT_MATTERMOST_SMART_MENTION_SYSTEM_PROMPT",
    "DEFAULT_SMART_MENTION_SYSTEM_PROMPT",
    "SmartMentionClassification",
    "SmartMentionConfig",
    "build_smart_mention_messages",
    "default_smart_mention_system_prompt",
    "format_recent_context_for_agent",
    "normalize_smart_mention_config",
    "parse_smart_mention_response",
    "truncate_text",
]
