import structs
import story
import loot
import log
import utils
import inputs
import math


def combat(
    player: structs.Player,
    world: structs.World,
    stats: structs.Statistics,
):
    chance = utils.combat_chance(player, world)
    success_bool, success_prob = utils.skill_check(utils.power_ratio(player, world), world.BeatDC)
    print(success_prob)
    success = success_bool
    stats.SuccessChanceCombat = success_prob
    stats.Success = success

    if success:
        chance = utils.death_chance(player, world)
        death = utils.chance(chance)
        stats.DeathChance = chance
        stats.Death = death

        if not death:
            exp = math.floor(
                utils.skill_difficulty(player, world) * inputs.BASE_XP_COMBAT
            )
            player.award_exp(exp)
            stats.XP_Earned = exp

            # gold = inputs.GOLD_PER_COMBAT_STEP
            gold = player.get_combat_gold() * (1 if success else -1)
            player.award_gold(int(gold))
            stats.Gold_Earned = gold

            drop = loot.get_drop(world)
            if drop is not None:
                player.award_loot(drop)
                stats.DropID = drop.ItemID


def non_combat(
    player: structs.Player,
    world: structs.World,
    stats: structs.Statistics,
):
    category = utils.non_combat_category(world)
    stats.OutcomeCategory = category.OutcomeCategory
    stats.SkillDifficulty = category.CategoryDC

    stat = player.get_stat(category.StatKey)
    stats.BaseStat = stat.Base
    stats.PerLevel = stat.PerLevel

    chance = utils.non_combat_chance(player, world, category.OutcomeCategory)
    success = utils.chance(chance)
    stats.StatScore = utils.stat_score(player, category.StatKey)
    stats.SuccessChance_NonCombat = chance
    stats.Success = success

    rules = utils.get_category_rules(category)
    exp = math.floor(utils.skill_difficulty(player, world) * inputs.BASE_XP_NON_COMBAT * (rules.XP_Success if success else rules.XP_Fail))
    player.award_exp(exp)
    stats.XP_Earned = exp

    # if success:
        # print(rules.Gold_Success)
    gold = player.get_non_combat_gold() * (rules.Gold_Success if success else rules.Gold_Fail) #inputs.GOLD_PER_NON_COMBAT_STEP
    player.award_gold(int(gold))
    stats.Gold_Earned = gold


def simulate(turns: int):
    player = structs.Player()
    world = story.create_world()

    for turn in range(turns):
        stats = structs.Statistics()

        # decide action
        if utils.chance(inputs.COMBAT_CHANCE):
            combat(player, world, stats)
        else:
            non_combat(player, world, stats)

        # change stage
        world = story.progress_story(turn, world)

        # record results
        log.record_turn(turn, player, world, stats)
