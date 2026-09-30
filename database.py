# Local reference data used by the Game Performance Analyzer.
# Keeping the data here makes it easy to update the supported hardware and games.

# CPU details used for the basic capability check.
CPUS = {
    "Intel Core i5-8250U": {
        "cores": 4,
        "threads": 8,
        "tier": 2
    },
    "Intel Core i5-12450H": {
        "cores": 8,
        "threads": 12,
        "tier": 5
    },
    "AMD Ryzen 5 5600H": {
        "cores": 6,
        "threads": 12,
        "tier": 5
    },
    "AMD Ryzen 7 5800H": {
        "cores": 8,
        "threads": 16,
        "tier": 6
    }
}

# GPU details used when calculating the system capability.
GPUS = {
    "NVIDIA MX110": {
        "vram_gb": 2,
        "tier": 2,
        "relative_score": 25
    },
    "NVIDIA GTX 1650": {
        "vram_gb": 4,
        "tier": 4,
        "relative_score": 50
    },
    "NVIDIA RTX 3050": {
        "vram_gb": 4,
        "tier": 5,
        "relative_score": 65
    },
    "NVIDIA RTX 4050": {
        "vram_gb": 6,
        "tier": 6,
        "relative_score": 80
    },
    "NVIDIA RTX 4060": {
        "vram_gb": 8,
        "tier": 7,
        "relative_score": 90
    },
    "AMD Radeon RX 6600": {
        "vram_gb": 8,
        "tier": 6,
        "relative_score": 75
    }
}

# Game profiles used to set the target FPS for the analysis.
GAMES = {
    "Valorant": {
        "genre": "Competitive",
        "target_fps": 60
    },
    "Minecraft": {
        "genre": "Sandbox",
        "target_fps": 60
    },
    "Grand Theft Auto V": {
        "genre": "Open World",
        "target_fps": 60
    },
    "Cyberpunk 2077": {
        "genre": "Open World",
        "target_fps": 60
    },
    "Among Us": {
        "genre": "Casual",
        "target_fps": 60
    }
}
