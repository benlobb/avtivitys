def on_a_pressed():
    if mySprite.overlaps_with(button):
        button.say(randomactivity, 4000)
    else:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

randomactivity = ""
button: Sprite = None
mySprite: Sprite = None
scene.set_background_color(8)
mySprite = sprites.create(img("""
        . . . . . . . e c 7 . . . . . . 
            . . . . e e e c 7 7 e e . . . . 
            . . c e e e e c 7 e 2 2 e e . . 
            . c e e e e e c 6 e e 2 2 2 e . 
            . c e e e 2 e c c 2 4 5 4 2 e . 
            c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
            c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
            c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
            . e e e 2 2 2 2 2 2 2 2 2 4 e . 
            . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
            . . 2 e e 2 2 2 2 2 4 4 2 e . . 
            . . . 2 2 e e 4 4 4 2 e e . . . 
            . . . . . 2 2 e e e e . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
button = sprites.create(img("""
        .2222222222222222222222222222222222222.
            227777222222222222222222222222227222222
            272222222222222222222222222222227222222
            272222222722722222272272222222277722722
            272772227272777222727277722227227227272
            272227227772722722777272272777227227772
            272227227222722722722272222727227227222
            227772222772722722277272222777227222772
            .2222222222222222222222222222222222222.
    """),
    SpriteKind.player)
mySprite.y = 100
mySprite.set_stay_in_screen(True)

def on_on_update():
    global randomactivity
    if Math.percent_chance(2.5):
        randomactivity = "Play outside."
    elif Math.percent_chance(2.5):
        randomactivity = "Make crafts."
    elif Math.percent_chance(2.5):
        randomactivity = "Build LEGOs."
    elif Math.percent_chance(2.5):
        randomactivity = "Skating."
    elif Math.percent_chance(2.5):
        randomactivity = "Send a letter to grand-parents."
    elif Math.percent_chance(2.5):
        randomactivity = "Play prodigy."
    elif Math.percent_chance(2.5):
        randomactivity = "Watch Nat. Geo. Kids. "
    elif Math.percent_chance(2.5):
        randomactivity = "Help mom/dad. "
    elif Math.percent_chance(2.5):
        randomactivity = "Write in a journal."
    elif Math.percent_chance(2.5):
        randomactivity = "Sew. "
    elif Math.percent_chance(2.5):
        randomactivity = "Write a story."
    elif Math.percent_chance(2.5):
        randomactivity = "Make movies. "
    elif Math.percent_chance(2.5):
        randomactivity = "Play piano."
    elif Math.percent_chance(2.5):
        randomactivity = "Jump on the trampoline."
    elif Math.percent_chance(2.5):
        randomactivity = "Play with/Call a friend."
    elif Math.percent_chance(2.5):
        randomactivity = "Play with/Call a friend."
    elif Math.percent_chance(2.5):
        randomactivity = "Read."
    elif Math.percent_chance(2.5):
        randomactivity = "Teach Carson the alphabet."
    elif Math.percent_chance(2.5):
        randomactivity = "Youtube art class"
    elif Math.percent_chance(2.5):
        randomactivity = "Make a treasure map."
    elif Math.percent_chance(2.5):
        randomactivity = "Organize your room."
    elif Math.percent_chance(2.5):
        randomactivity = "Color."
    elif Math.percent_chance(2.5):
        randomactivity = "Play with Carson."
    elif Math.percent_chance(2.5):
        randomactivity = "Make a smoothie."
    elif Math.percent_chance(2.5):
        randomactivity = "Eating fruit."
    elif Math.percent_chance(2.5):
        randomactivity = "Catch lizards."
    else:
        pass
game.on_update(on_on_update)
