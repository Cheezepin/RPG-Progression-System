# RPG Progression System

A Python-based simulation system for modeling and balancing RPG progression mechanics, including combat, loot, experience, and story progression.

## Overview

This project simulates a player's journey through an RPG campaign, tracking progression through levels, equipment, and story beats. It's designed to help game designers test and balance progression curves, difficulty scaling, and reward systems before implementing them in a game.

## Features

- **Player Progression Simulation**: Models XP gain, leveling, and character growth with configurable XP curves
- **Combat & Non-Combat Systems**: Simulates both combat encounters and skill-based challenges with dynamic success rates
- **Death & Repair System**: Includes death mechanics with equipment repair costs and gold penalties
- **Loot System**: Equipment generation with quality tiers (Common/Rare/Epic/Legendary) and item power scaling across zones
- **Multi-Tier Gear System**: Zone-based gear tiers (T1-T4) with different quality distributions
- **Story Beat Integration**: Follows the Hero's Journey structure with configurable story stages
- **JSON-Based Configuration**: Primary configuration via `Inputs.json` with comprehensive parameter control
- **Regression Testing**: Built-in assertion and regression testing framework for balance validation
- **Detailed Data Logging**: Outputs detailed simulation results with turn-by-turn tracking
- **Data Dictionary**: Comprehensive documentation of all data fields and calculations

## Project Structure

```
RPG-Progression-System/
├── main.py                   # Entry point for running simulations
├── simulate.py               # Core simulation loop and encounter logic
├── structs.py                # Data structures (Player, World, Equipment, etc.)
├── story.py                  # Story beat progression logic
├── loot.py                   # Loot generation and drop tables
├── parser.py                 # CSV parsing utilities
├── log.py                    # Data logging for analysis
├── utils.py                  # Helper functions
├── inputs.py                 # Input parameter constants
├── params.py                 # Simulation parameter constants
└── data/
    ├── Inputs.json           # Primary configuration file (JSON)
    ├── Progression.csv       # Level and XP curve definitions
    ├── Params.csv            # Tunable simulation parameters
    ├── StoryBeats.csv        # Story stage definitions
    ├── Stats.csv             # Player stat configurations
    ├── LootTable.csv         # Item drop tables
    ├── NonCombat.csv         # Non-combat challenge definitions
    ├── NC_Categories.csv     # Non-combat category definitions
    ├── NC_Rules.csv          # Non-combat rule configurations
    ├── Curve.csv             # Progression curve data
    ├── Simulator.csv         # Simulation output and state tracking
    ├── Dashboard.csv         # High-level simulation metrics
    ├── Assertions.csv        # Test assertions for validation
    ├── REGRESSION.csv        # Regression test results
    ├── DebugConfig.csv       # Debug configuration settings
    └── DATA_DICTIONARY.csv   # Documentation of all data columns
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/RPG-Progression-System.git
cd RPG-Progression-System
```

2. Ensure you have Python 3.10+ installed (requires match/case syntax)

3. No external dependencies required - uses Python standard library only

## Usage

### Basic Simulation

Run a basic simulation with default settings:

```bash
python main.py
```

This will run a 50-step simulation using the default configuration from `data/Inputs.json`.

### Custom Configuration

Modify `main.py` to customize the number of simulation steps:

```python
import simulate

if __name__ == "__main__":
    simulate.simulate(50)  # Run for 50 turns
```

To adjust simulation parameters, edit the configuration files:

- **`data/Inputs.json`**: Primary configuration for all simulation parameters
- **`inputs.py`**: Python constants loaded from Inputs.json
- **`params.py`**: Simulation algorithm parameters (success rates, slopes, etc.)

### Configuration Files

#### Inputs.json (Primary Configuration)

The main configuration file containing all simulation parameters in JSON format:

**Parameters Section:**

- `XPExponent`: Experience curve steepness (default: 1.35)
- `CombatChance`: Probability of combat encounter (0-1, default: 0.6)
- `DeathChance`: Base chance of death in combat (default: 0.08)
- `RepairCostPct`: Equipment repair cost percentage (default: 0.05)
- `BaseXP_Combat/NonCombat`: Base XP rewards
- `ZoneTier`: Starting zone tier
- `StepCount`: Default simulation length
- `Seed`: Random seed for reproducibility

**GearQualityWeights:** Drop rates for Common/Rare/Epic/Legendary items per tier (T1-T4)

**DropThresholds:** Probability thresholds for equipment slot drops

**ScoreWeights:** Scoring multipliers for quality tiers and zone scaling

#### Progression.csv

Defines level progression and rewards:

- `Level`: Character level
- `XP_to_Next`: Experience required to reach next level
- `Gold_Combat`: Gold earned from combat encounters
- `Gold_NonCombat`: Gold earned from non-combat encounters

#### Params.csv

Tunable parameters for difficulty and progression:

- `FLOOR_SUCCESS`: Minimum success chance (default: 0.05)
- `CEIL_SUCCESS`: Maximum success chance (default: 0.95)
- `ATTEMPT_SLOPE`: Difficulty scaling factor
- `COMBAT_SLOPE`: Combat difficulty curve (default: 0.55)
- `NC_SLOPE`: Non-combat difficulty curve (default: 1.3)
- `FAIL_STEP`: Difficulty increase on failure
- `SUCCESS_STEP`: Difficulty change on success

#### StoryBeats.csv

Defines narrative progression using Hero's Journey structure:

- `BeatNum`: Sequential beat number
- `Stage`: Story stage name
- `BeatName`: Descriptive name for the beat
- `BeatStartStep`: Turn when this beat becomes active
- `ZoneLevel`: Recommended character level
- `BeatDC`: Difficulty class for challenges

#### DATA_DICTIONARY.csv

Complete documentation of all data columns used across the simulation system. Reference this file to understand the purpose and usage of any field in the output files.

## Core Modules

### inputs.py

Python constants module containing all primary simulation parameters loaded from `Inputs.json`:

- Economy parameters (repair costs, vendor taxes, respec costs)
- Experience and leveling parameters
- Combat and death mechanics
- Zone and gear scaling factors
- Random seed configuration

### params.py

Algorithm-specific parameters controlling simulation behavior:

- Success rate floors and ceilings
- Difficulty slopes for combat and non-combat encounters
- Combat shift and scaling factors
- Live roll settings

### simulate.py

Main simulation engine that orchestrates the turn-by-turn progression:

- Encounter generation (combat vs non-combat)
- Success/failure resolution
- Loot generation and distribution
- Player state updates

### structs.py

Core data structures:

- `Player`: Character state, equipment, and resources
- `World`: Story beats, zones, and environmental state
- `Equipment`: Item management and power calculations
- `Inputs`: Configuration data container

## Data Structures

### Player

- Experience and level tracking
- Equipment system (Weapon, Helm, Chest, Legs, Accessory)
- Loot inventory
- Gold accumulation
- Gear score calculation

### World

- Current story beat
- Zone difficulty and tier
- Stage progression

### Equipment

- Slot-based equipment system (5 slots)
- Item power calculation with quality modifiers
- Zone-scaled item generation
- Auto-equip best items by power

## Output

Simulation results are logged to multiple CSV files in the `data/` directory:

### Simulator.csv

Detailed turn-by-turn simulation log including:

- Player progression (XP, levels, gear score)
- Combat and non-combat encounter results
- Success/failure rates and power ratios
- Equipment drops and upgrades
- Resource accumulation (gold, reputation)
- Death events and repair costs

### Dashboard.csv

High-level metrics and summary statistics for quick analysis:

- Overall progression rates
- Success rate trends
- Economy balance metrics
- Gear progression summary

### Assertions.csv / REGRESSION.csv

Test validation and regression testing results to ensure simulation consistency across runs

## Configuration Tips

### Adjusting Difficulty

- Modify `COMBAT_SLOPE` and `NC_SLOPE` in `params.py` to change how difficulty scales with power differences
- Adjust `FLOOR_SUCCESS` and `CEIL_SUCCESS` to set minimum/maximum success rates
- Change `DeathChance` in `Inputs.json` to control combat lethality

### Tuning Progression Speed

- Adjust `XPExponent` to change how quickly level requirements increase
- Modify `BaseXP_Combat` and `BaseXP_NonCombat` for faster/slower leveling
- Edit `Progression.csv` to customize level-by-level XP requirements

### Balancing Economy

- Set `RepairCostPct` to control the cost of dying
- Adjust `VendorTaxPct` for selling item penalties
- Modify gold rewards in `Progression.csv` per level

### Loot Drop Rates

- Edit `GearQualityWeights` in `Inputs.json` to change rarity distributions per tier
- Adjust `DropThresholds` to control which equipment slots drop more frequently
- Modify `ScoreWeights` to balance item power calculations

## Use Cases

- **Game Balance Testing**: Test XP curves and progression pacing across multiple zones
- **Difficulty Tuning**: Adjust encounter difficulty and success rates using power-based formulas
- **Economy Design**: Balance gold rewards, repair costs, and loot drop rates
- **Narrative Pacing**: Ensure story beats align with player power levels using zone tiers
- **Regression Testing**: Validate balance changes don't break intended progression
- **Data Analysis**: Export simulation results for statistical analysis and visualization
