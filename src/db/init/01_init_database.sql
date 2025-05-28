-- Create Salem Tables

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,
    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    gold INTEGER DEFAULT 100,
    wand TEXT,
    inventory JSONB DEFAULT '[]'::JSONB,
    quests JSONB DEFAULT '[]'::JSONB,
    achievements JSONB DEFAULT '[]'::JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);