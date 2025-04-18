def on_button_multiplayer_a_pressed(player2):
    mp.get_player_sprite(player2).vy = -200
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(sprite, effects.fire, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.finish, on_on_overlap2)

projectile: Sprite = None
playerImages = [assets.image("""
        red duck
        """),
    assets.image("""
        blue duck
        """),
    assets.image("""
        orange duck
        """)]

def on_wrap1():
    for index in range(3):
        mp.set_player_sprite(mp.get_player_by_index(index),
            sprites.create(playerImages[index], SpriteKind.player))
        mp.get_player_sprite(mp.get_player_by_index(index)).x = 75 + -30 * index
        mp.get_player_sprite(mp.get_player_by_index(index)).ay = 600
        mp.get_player_sprite(mp.get_player_by_index(index)).set_stay_in_screen(True)
bundles.wrap1(on_wrap1)

finish = sprites.create(assets.image("""
    finish
    """), SpriteKind.finish)
info.set_life(5)
finish.x = 0

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(assets.image("""
        fireball
        """), -75, 0)
    projectile.y = randint(0, 120)
game.on_update_interval(500, on_update_interval)
