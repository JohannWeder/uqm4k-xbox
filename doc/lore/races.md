# Races, Ships and Captains

A reference to the 25 starfaring races you can fly in *The Ur-Quan Masters*:
their ships, combat stats, in-game captain names, and what the game's dialogue
reveals about them. For the opening background, see
[background-story.md](background-story.md).

> **Spoiler warning:** the *Lore* sections draw on the full dialogue scripts and
> reveal much of the main plot.

## Index

| Race | Ship | Melee cost | Side in the War |
|---|---|---|---|
| [Androsynth](#androsynth) | Guardian | 15 | Hierarchy |
| [Arilou](#arilou-ariloulaleelay) | Skiff | 16 | Alliance |
| [Chenjesu](#chenjesu) | Broodhome | 28 | Alliance |
| [Chmmr](#chmmr) | Avatar | 30 | — (appears during the game) |
| [Druuge](#druuge) | Mauler | 17 | Independent |
| [Earthling](#earthling-human) | Cruiser | 11 | Alliance |
| [Ilwrath](#ilwrath) | Avenger | 10 | Hierarchy |
| [Kohr-Ah](#kohr-ah) | Marauder | 30 | Ur-Quan faction |
| [Melnorme](#melnorme) | Trader | 18 | Independent |
| [Mmrnmhrm](#mmrnmhrm) | X-Form | 19 | Alliance |
| [Mycon](#mycon) | Podship | 21 | Hierarchy |
| [Orz](#orz) | Nemesis | 23 | Independent |
| [Pkunk](#pkunk) | Fury | 20 | Independent |
| [Shofixti](#shofixti) | Scout | 5 | Alliance |
| [Slylandro](#slylandro) | Probe | 17 | Independent |
| [Spathi](#spathi) | Eluder | 18 | Hierarchy |
| [Supox](#supox) | Blade | 16 | Independent |
| [Syreen](#syreen) | Penetrator | 13 | Alliance |
| [Thraddash](#thraddash) | Torch | 10 | Independent |
| [Umgah](#umgah) | Drone | 7 | Hierarchy |
| [Ur-Quan](#ur-quan-kzer-za) | Dreadnought | 30 | Hierarchy (masters) |
| [Utwig](#utwig) | Jugger | 22 | Independent |
| [VUX](#vux) | Intruder | 12 | Hierarchy |
| [Yehat](#yehat) | Terminator | 23 | Alliance |
| [Zoq-Fot-Pik](#zoq-fot-pik) | Stinger | 6 | Independent |

## Reading the stats

The numbers are the constants in each ship's source file
(`src/uqm/ships/<race>/<race>.c`; a few folders are abbreviated, such as
`androsyn`, `blackurq` for the Kohr-Ah, `slylandr`, `thradd` and `zoqfot`).

- **Crew** is the ship's hit points; **Battery** powers its weapons.
- **Frames** are battle frames, 24 per second. *Energy regen* "1 per 8 frames"
  means one battery point every 8 frames; *turn delay* is how many frames pass
  between steps of rotation (lower turns faster).
- **Max speed** and **acceleration** are in the engine's internal world units.
  They compare ships with each other rather than measuring anything real.
- **Melee cost** is the ship's point value when building a Super Melee fleet.
- Where the code defines a value through another constant, it's shown
  resolved, with the constant in brackets: `MAX_CREW_SIZE` and
  `MAX_ENERGY_SIZE` are both 42.

Weapon descriptions come from the game manual
([`doc/release/UQM-Manual.txt`](../release/UQM-Manual.txt)). Captain names come
from `content/base/ships/<race>/*.txt`; the game picks one at random for each
ship. Lore comes from the dialogue scripts in `content/base/comm/`.

---

## Androsynth

**Ship:** Androsynth Guardian · **Melee cost:** 15

"Pokey. Blows mean bubbles. Changes to flaming comet."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 24 |
| Energy regen | 1 per 8 frames |
| Max speed | 24 |
| Acceleration | 3 per 0 frames |
| Turn delay | 4 frames |
| Mass | 6 |
| Weapon / special cost | 3 / 2 |

**Primary:** Fires homing acid bubble clouds.
**Secondary:** Transforms into the 'Blazer', a comet that does considerable damage by ramming its opponents.

**Captains:** BOOJI-1, DORN-3, BIM-XT, JOR-15, 976-KILL, KORB-7B, XR4-TI, CRC-16, BHS-79, DOS-1.0, ME-262, AK-47, 1040-EZ, NECRO-99, HAL-2001, SR-71

### Lore

The Androsynth are humanoid clones (the Spathi call them "the humanoid clones you call Androsynth") whose home star is Eta Vulpeculae. The starbase veterans admit that the Androsynth "had a damn good reason for hating us": humans had kept them as slaves for nearly 50 years. Their stars fell to the Ur-Quan at about the time Earth and the Chenjesu formed the Alliance of Free Stars, and they fought as Hierarchy battle thralls. Human pilots on the Coreward Front feared nothing more than the Androsynth Hit-And-Run Squadron, whose Blazers were "more than a match for our Cruisers". Their hostile presence near Vulpeculae also cut short a Chenjesu historian's research into the ancient Taalo.

After the war, according to the Melnorme, the Androsynth began experimenting with Inter-Dimensional Fatigue and had just made a major breakthrough when they were wiped out by the Orz, "who appeared seemingly out of nowhere". Nobody knows exactly what happened, only that the Androsynth are "all gone". The Arilou say the Androsynth "showed themselves, and something noticed them. There are no more Androsynth now. Only Orz." The Orz say the Androsynth "made some *slippery places*" that let the Orz *smell* this reality, that they are trying to *pull* the Androsynth, and they refuse to say more ("No more Androsynth is better"). By the time of the game, Androsynth space is Orz space. The Androsynth have no dialogue of their own. Commander Hayes also recalls rumors that Corridor Nine ran a secret operation near Androsynth space, in the direction of the Vela colony.

*Sources:* `content/base/ships/androsynth/guardian.txt`, `src/uqm/ships/androsyn/androsyn.c`, `doc/release/UQM-Manual.txt`, `content/base/comm/starbase/starbase.txt`, `content/base/comm/melnorme/melnorme.txt`, `content/base/comm/arilou/arilou.txt`, `content/base/comm/orz/orz.txt`, `content/base/comm/safeones/safeones.txt`, `content/base/comm/commander/commander.txt`

---

## Arilou (Ariloulaleelay)

**Ship:** Arilou Skiff · **Melee cost:** 16

"Fast, no inertia. Auto-aim laser. Hyper-jump."

| Stat | Value |
|---|---|
| Crew (max) | 6 |
| Battery (max) | 20 |
| Energy regen | 1 per 6 frames |
| Max speed | 40 |
| Acceleration | 40 (= MAX_THRUST) per 0 frames |
| Turn delay | 0 frames |
| Mass | 1 |
| Weapon / special cost | 2 / 3 |

**Primary:** Auto-aiming, short-range laser.
**Secondary:** Random teleport. (Note: the Skiff has no inertia and stops instantly when thrust is released.)

**Captains:** Fefaloo, Bezabu, Tiptushi, Marypup, Tinkafo, Patooti, Tifiwilo, Loleelu, Louifoui, Pinywiny, Oowbabe, Dingdup, Wewalia, Yipyapi, Ropilup, Wolwali

### Lore

The Arilou Lalee'lay got their name from "the children of the Celts". Starbase records note that they match almost exactly the aliens of 20th-century UFO reports: white skin, minimal features, and huge glowing almond-shaped eyes. They are fond of humans in a condescending, unsettling way. They call the captain "child" and humanity their "extended family". They say they have visited Earth for thousands of years and made "modifications": they examined people, inspired cave paintings, standing stones, pyramids and crop circles, and worked to make humanity "invisible" to parasitic beings "Beyond". They warn that the Androsynth drew such attention to themselves, and they say the Orz are dangerous. They do not come from normal space. Their homeworld, Falayalaralfali, lies in QuasiSpace, a dimension next to HyperSpace, and they travel between realities through Portals.

The Arilou appeared at Earth and joined the Alliance of Free Stars the day after humanity did (the starbase dates this to 2116). They left once Earth was safe under the slave shield, an idea they "rather liked" and wished they had thought of themselves. Some Alliance veterans found them creepy but envied how fast they moved through HyperSpace. In the game they will not fight, but they share knowledge. They took an injured Talking Pet from an Ur-Quan wreck at Alpha Pavonis VII and left it with the Umgah, later realize it is a Dnyarri, and offer to build a Portal Spawner for the flagship if the captain brings them that wreck's Warp Pod. The Arilou have no individual named speaker.

*Sources:* `content/base/ships/arilou/skiff.txt`, `src/uqm/ships/arilou/arilou.c`, `doc/release/UQM-Manual.txt`, `content/base/comm/arilou/arilou.txt`, `content/base/comm/starbase/starbase.txt`, `content/base/comm/melnorme/melnorme.txt`

---

## Chenjesu

**Ship:** Chenjesu Broodhome · **Melee cost:** 28

"Big. Crystal fragment weapon. Breeds pesky doggies."

| Stat | Value |
|---|---|
| Crew (max) | 36 |
| Battery (max) | 30 |
| Energy regen | 1 per 4 frames |
| Max speed | 27 |
| Acceleration | 3 per 4 frames |
| Turn delay | 6 frames |
| Mass | 10 |
| Weapon / special cost | 5 / 30 (= MAX_ENERGY) |

**Primary:** Crystal Shard. Travels until the fire button is released, then shatters.
**Secondary:** De-energizing Offensive Guided Interceptor. Launches an autonomous DOGI that rams the opponent to drain their combat batteries.

**Captains:** Kzzakk, Tzrrow, Zzmzmm, Vziziz, Hmmhmm, Bzrak, Krrtzz, Zzzzz, Zxzakz, Brrzap, Tzaprak, Pzkrakz, Fzzzz, Vrroww, Zznaz, Zzzhmm

### Lore

The Chenjesu are a crystalline, silicon-based race from Procyon. Humans credited them with "fantastic intellects", possibly the product of an ancient, peaceful culture. They can send HyperWave messages naturally, and their natural receptors are more sensitive than the best human equipment. In 2098 those receptors picked up the Ur-Quan's "exulting hunting cry" from Ophiuchi. When the Ur-Quan conquered the Umgah and attacked the Ilwrath, the Chenjesu and Mmrnmhrm put together a defense force. The Chenjesu reached Earth in 2112, and humanity joined them to form the Alliance of Free Stars (the agreement is dated 2116). They led the Alliance in practice but never formally accepted the title, and one starbase officer says he would "rather be taking orders from a Chenjesu than any other lifeform". The bulk of the Ilwrath fleet was sent against them and the Mmrnmhrm.

Holding Rigel cost the Chenjesu dearly. The Ur-Quan then turned their main forces on Procyon, where the Sa-Matra battle platform "incinerated our finest broodhome vessels from ten times our own ships' weapon range." Before they surrendered, the Chenjesu sent Earth a last message advising it to accept slavery until the Sa-Matra could be destroyed. Afterwards they and the Mmrnmhrm chose to share a single slave shield on Procyon so they could merge into a hybrid race (see Chmmr). The Chenjesu have no dialogue of their own. Before the merger is finished they speak jointly in lowercase ("we are the chenjesu... we are the mmrnmhrm"). Other characters mention the Chenjesu historian Tzzz-Tzer-Tzak, and the Melnorme note that the ancient Taalo were also silicon-based but "bore little resemblance to the modern Chenjesu".

*Sources:* `content/base/ships/chenjesu/broodhome.txt`, `src/uqm/ships/chenjesu/chenjesu.c`, `doc/release/UQM-Manual.txt`, `content/base/comm/starbase/starbase.txt`, `content/base/comm/chmmr/chmmr.txt`, `content/base/comm/melnorme/melnorme.txt`

---

## Chmmr

**Ship:** Chmmr Avatar · **Melee cost:** 30

"Very powerful laser. ZapSats. Tractor beam."

| Stat | Value |
|---|---|
| Crew (max) | 42 (MAX_CREW_SIZE) |
| Battery (max) | 42 (MAX_ENERGY_SIZE) |
| Energy regen | 1 per 1 frames |
| Max speed | 35 |
| Acceleration | 7 per 5 frames |
| Turn delay | 3 frames |
| Mass | 10 |
| Weapon / special cost | 2 / 1 |

**Primary:** Immensely powerful short-range laser.
**Secondary:** Tractor beam. (Note: three orbiting "ZapSats" attack anything that comes in range.)

**Captains:** Mnzgk, Chzrmn, Bzztrm, Zrnzrk, Tzzqrn, Kzzrn, Vzrzn, Qrntz, Rmnzk, Szmrnz, Zbzzn, Frnkzk, Prmtzz, Tzrtzn, Kztztz, Mrnkzt

### Lore

The Chmmr are a hybrid of the crystalline Chenjesu and the purely mechanical Mmrnmhrm. After their defeat in 2135 the two races sealed themselves under one slave shield on Procyon and began "the process": a synthesis of both species and cultures, powered only by sunlight, that would take about 35 Earth years. When it was done they planned to break the shield "like a winged insect unleashed from its cocoon" and face the Ur-Quan and the Sa-Matra. While still under the shield they speak in a quiet joint voice. They find the captain's visit "painful", refuse to speed things up because it could fail catastrophically, and still give advice: to beat the Ur-Quan, destroy the Sa-Matra with a planet-killing weapon and a distraction.

If the captain floods their synthesis machinery with radiant energy (using the precursor energy device taken from the Mycon), the process that should have taken decades finishes in seconds. The Chmmr burst free, incomplete, and speak in all capitals ("WE ARE FREE!... WE ARE THE CHMMR."). They become the captain's main strategic advisors. They read the flagship's logs and locate the Sa-Matra near Crateris. They identify the Dnyarri (made harmless by the Taalo device) as the psychic distraction and the Utwig bomb as the weapon, and boost the bomb with their crystal technology, warning that it will annihilate the flagship. They also hand over the design for the Avatar, which they say is "much more effective than our broodhome or X-Form vessels", along with Chmmr crews. The Chmmr speak only as a collective, with no named individuals.

*Sources:* `content/base/ships/chmmr/avatar.txt`, `src/uqm/ships/chmmr/chmmr.c`, `src/uqm/element.h`, `doc/release/UQM-Manual.txt`, `content/base/comm/chmmr/chmmr.txt`, `content/base/comm/melnorme/melnorme.txt`

---

## Druuge

**Ship:** Druuge Mauler · **Melee cost:** 17

"Sluggish. Heavy momentum weapon. Combustible crew."

| Stat | Value |
|---|---|
| Crew (max) | 14 |
| Battery (max) | 32 |
| Energy regen | 1 per 50 frames |
| Max speed | 20 |
| Acceleration | 2 per 1 frames |
| Turn delay | 4 frames |
| Mass | 5 |
| Weapon / special cost | 4 / 16 |

**Primary:** Long-range, high-recoil cannon.
**Secondary:** Sets one crew member on fire to gain combat energy.

**Captains:** Tuuga, Siinur, Kaapo, Juugl, Paato, Feezo, Maad, Moola, Kooli, Faazur, Zooto, Biitur, Duulard, Piini, Soopi, Peeru

### Lore

The Druuge are a society run as a single business, the Crimson Corporation ("we ARE the Crimson Corporation, and the Crimson Corporation is us"). Their Central Trade World is Zeta Persei I. Everything on their world belongs to the Corporation, so a laid-off employee is "stealing Corporation property such as air and sunlight" and is sent to "feed the furnace". The same fate awaits any trader who makes a bad deal. They openly embrace greed ("We acknowledge our greed. We revel in it.") and have a written contract with their god. Under Druuge Statute 3429, subsection A86, any unarmed ship is a derelict that anyone may salvage. They mock the Melnorme as profiteers and pirates.

Their dialogue does not place them on either side of the Alliance–Hierarchy war; they appear as independent traders. They pay in crew: the captain can trade crew for fuel, Mauler starships and "Precursor" artifacts (the Rosy Sphere, the Glowing Rod and the Trident of Wimbli). They insist this is not slave trading. They also want Shofixti maidens (to breed furnace workers), Mycon egg cases, a Vortex Spawner and a HyperWave 'Caster. They boast of having "diverted" the approaching Kohr-Ah, whom they first heard about from their "ex-clients" the Burvixese. In one storyline, a Druuge captain claims the Utwig Precursor bomb. He explains that the Druuge sold the Utwig the worthless Ultron, were "paid" with a vault of junk, and now want the weapon as their rightful price. The Druuge have no individually named speaker.

*Sources:* `content/base/ships/druuge/mauler.txt`, `src/uqm/ships/druuge/druuge.c`, `doc/release/UQM-Manual.txt`, `content/base/comm/druuge/druuge.txt`

---

## Earthling (Human)

**Ship:** Earthling Cruiser · **Melee cost:** 11

"Slow, heavy. Seeking nukes. Point defense lasers."

| Stat | Value |
|---|---|
| Crew (max) | 18 |
| Battery (max) | 18 |
| Energy regen | 1 per 8 frames |
| Max speed | 24 |
| Acceleration | 3 per 4 frames |
| Turn delay | 1 frames |
| Mass | 6 |
| Weapon / special cost | 9 / 4 |

**Primary:** Homing nuclear missile.
**Secondary:** Point-defense laser.

**Captains:** Decker, Trent, Adama, Spiff, Graeme, Kirk, Pike, Halleck, Tuf, Pirx, Wu, VanRijn, Ender, Buck, Solo, Belt

### Lore

Humanity entered the war late. The Chenjesu reached the solar system in 2112, and Earth joined them to found the Alliance of Free Stars (the agreement is dated 2116). Earth restarted its mothballed heavy industry and built hundreds of heavy Cruisers. Its biggest mistake of the war was the botched first contact with the VUX in 2119, when Captain Jeffry L. Rand of the *Far Voyager* accidentally insulted a VUX commander. Humans fought on the Coreward Front for about ten years. In 2134 the Alliance was pushed back past Raynet, and after Procyon fell, Earth was overrun: Ceres Station and the lunar laser-forts were lost, and Buenos Aires was destroyed as an example. Given the choice by popular vote, Earth refused to serve as a battle thrall and became a "fallow" slave world under a red slave shield. Before raising the shield, the Ur-Quan destroyed every human structure more than 500 years old, along with mysterious sites in Iraq, the Amazon, Antarctica and the Atlantic seabed. The starbase crew also admit an earlier sin: their grandparents kept the Androsynth clones as slaves for nearly 50 years.

The main human character is Starbase Commander Hayes, a Coreward Front veteran. When the game begins, his roughly 1,900-person orbital station has gone eight years without an Ur-Quan resupply and is close to dying. The player captain is a human born on Unzervalt, the colony world at Vela, and comes from a Star Control science mission that Hayes had never heard of (he only recalls rumors of a Corridor Nine operation in that direction). The captain arrives in a Precursor starship and offers to rebuild the Alliance. Hayes first demands that the captain destroy the Hierarchy base on the Moon. After that the starbase becomes the player's home port, building ships, supplying crew, analyzing artifacts and briefing the captain on history. The captain also gets to name the new alliance.

*Sources:* `content/base/ships/human/cruiser.txt`, `src/uqm/ships/human/human.c`, `doc/release/UQM-Manual.txt`, `content/base/comm/commander/commander.txt`, `content/base/comm/starbase/starbase.txt`

---

## Ilwrath

**Ship:** Ilwrath Avenger · **Melee cost:** 10

"Large. Devastating flame blast. Cloaking device."

| Stat | Value |
|---|---|
| Crew (max) | 22 |
| Battery (max) | 16 |
| Energy regen | 4 per 4 frames |
| Max speed | 25 |
| Acceleration | 5 per 0 frames |
| Turn delay | 2 frames |
| Mass | 7 |
| Weapon / special cost | 1 / 3 |

**Primary:** Short-range flamethrower
**Secondary:** Cloaking device

**Captains:** Gorgon, Taragon, Kalgon, Borgo, Dirga, Slygor, Rogash, Argarak, Kayzar, Baylor, Zoggak, Targa, Vogar, Lurgo, Regorjo, Manglor

### Lore

The Ilwrath are spider-like beings with carapaces, mandibles, quills, regenerating appendages and a "sensory cluster". They proudly call themselves evil, and their whole culture is built around worshipping the twin death-gods Dogar ("the Killer in a Black Cloak") and Kazon ("the Great Deceiver") through torture, ritual sacrifice and self-mutilation. A priestly cabal once decided which gods were true and what the gods wanted. Their homeworld orbits the "Eye of Dogar". The Ur-Quan conquered the "hostile but weak" Ilwrath early on, and about 29 years before the game they upgraded the Ilwrath ships. The Ilwrath became eager Hierarchy battle thralls. They remember the war against the Alliance as a glorious feast. Starbase veterans remember Avengers that "could appear out of nowhere and melt a Cruiser down to slag in seconds". Most of the Ilwrath fleet was thrown against the Chenjesu and Mmrnmhrm.

When the Ur-Quan ordered that humans be left alive, the Ilwrath's planned "Mountains of Flesh" slaughter of Earth was called off. They then ran out of native species to torment, including the Grah, which were wiped out by a bureaucratic error. After that, "voices of their gods" on HyperWave Channel 44 sent them to hunt the Pkunk. The Melnorme reveal that the voices are really the Umgah playing a prank with a HyperWave 'Caster. The Ilwrath majority rose up and killed their whole priest caste when the priests called the signals blasphemous. Humans are a favourite prey animal for the Ilwrath, and every encounter is full of gleeful threats. The player can impersonate Dogar and Kazon on Channel 44 and send the Ilwrath to make war on the Thraddash. The dialogue names no individual Ilwrath commander.

*Sources:* content/base/ships/ilwrath/avenger.txt, src/uqm/ships/ilwrath/ilwrath.c, doc/release/UQM-Manual.txt, content/base/comm/ilwrath/ilwrath.txt, content/base/comm/melnorme/melnorme.txt, content/base/comm/starbase/starbase.txt

---

## Kohr-Ah

**Ship:** Kohr-Ah Marauder · **Melee cost:** 30

"Massive. Long-range spinning blades, ring of fiery death."

| Stat | Value |
|---|---|
| Crew (max) | 42 (MAX_CREW_SIZE) |
| Battery (max) | 42 (MAX_ENERGY_SIZE) |
| Energy regen | 1 per 4 frames |
| Max speed | 30 |
| Acceleration | 6 per 6 frames |
| Turn delay | 4 frames |
| Mass | 10 |
| Weapon / special cost | 6 / 21 (MAX_ENERGY_SIZE / 2) |

**Primary:** Spinning blades that stop and home when the fire button is released
**Secondary:** Fiery Ring of Inevitable and Eternal Destruction (F.R.I.E.D.), a short-range corona of energy that blocks shots and inflicts lots of damage

**Captains:** Death 11, Death 17, Death 37, Death 23, Death 7, Death 13, Death 19, Death 29, Death 31, Death 41, Death 43, Death 3, Death 5, Death 47, Death 53, Death 83

### Lore

The Kohr-Ah are the Black Ur-Quan. The Dnyarri bred them by genetic tinkering as the Ur-Quan "Effectuators": the builders, fighters, laborers and soldiers. The Green Ur-Quan, the Kzer-Za, were bred as the scientists and bureaucrats. After the slave revolt against the Dnyarri, a charismatic fleet officer named Kohr-Ah proposed that all non-Ur-Quan sentient life be wiped out. The Kzer-Za and the Melnorme call this the "Eternal Doctrine". The Kohr-Ah themselves call their creed the "Path of Now and Forever". The Kohr-Ah burned the Yuptar homeworld. The Kzer-Za, who wanted to enslave other races rather than destroy them, then confronted the Kohr-Ah in orbit above the last free race's world. In the Kohr-Ah account, that race was the one-eyed Mael-Num, who had pleaded "Why do you do this thing?". This began the first Doctrinal War. The Kzer-Za won with a Precursor battleship, the Sa-Matra, but spared the Kohr-Ah and exiled them to circle the galaxy in the opposite direction. Whenever the two branches meet, they fight a ritual war, and the winner takes the Sa-Matra.

During the game, that war is being fought around Crateris. The Kohr-Ah say they do not kill but "cleanse". They believe each death gives the victim a chance to be reborn as an Ur-Quan, and they boast that more than five thousand races have failed to stop them. A Kohr-Ah commander keeps a "trophy bone-pit" holding a skeleton of every race it has personally wiped out. Asked "Why do you do this thing?", the Kohr-Ah tell their full history: their friendship with the Taalo, the Dnyarri enslavement, and the years of agony under the Excruciators. The Kzer-Za mention a Kohr-Ah "Primat" (female). They warn that if the Kohr-Ah win, the Kzer-Za will stand aside while the Kohr-Ah cleanse every former Hierarchy slave race, Earth included. Late in the game the Kohr-Ah announce that they have won, and that they have destroyed the Starbase orbiting Earth.

*Sources:* content/base/ships/kohrah/marauder.txt, src/uqm/ships/blackurq/blackurq.c, src/uqm/element.h, doc/release/UQM-Manual.txt, content/base/comm/kohrah/kohrah.txt, content/base/comm/urquan/urquan.txt, content/base/comm/melnorme/melnorme.txt

---

## Melnorme

**Ship:** Melnorme Trader · **Melee cost:** 18

"Tubby. Chargeable weapon. Can disrupt enemy controls."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 42 (MAX_ENERGY_SIZE) |
| Energy regen | 1 per 4 frames |
| Max speed | 36 |
| Acceleration | 6 per 4 frames |
| Turn delay | 4 frames |
| Mass | 7 |
| Weapon / special cost | 5 / 20 |

**Primary:** Charged shot. The longer the fire button is held, the stronger the shot.
**Secondary:** Confusion beam that scrambles enemy controls.

**Captains:** Reddish, Orangy, Aqua, Crimson, Magenta, Cheruse, Beige, Fuchsia, Umber, Cerise, Mauve, Grayish, Yellow, Black, Bluish, Purple

### Lore

The Melnorme are travelling information merchants who have only recently arrived in this region of space. They take no side in the war between the Alliance and the Hierarchy. They will not discuss their own history, psychology, physiology, homeworlds or "potentially ominous, long-range plans", though they say all of it is for sale. They have given up currency and trade only in things of "intrinsic value". They think giving without fair exchange is vulgar. They buy biological data on alien life, the locations of "Rainbow worlds" and Precursor artifacts, paying in Interstar Credits. In return they sell fuel, ship technology (such as Hellbore Cannons and Shiva Furnaces) and a long run of facts about current events, alien races and galactic history. Most of what humans know about the Ur-Quan's past comes from them. They also rescue stranded captains, for a fee. Their bridge lighting changes colour with their mood (blue, for example, means a threat), and their captains are named after colours.

The player's usual contact is Trade Master Greenish of the starship "Inevitably Successful in All Circumstances", who once mentions a subordinate named Ochre. Greenish owns a "MetaChron", an alien artifact that is slowly darkening, which he takes as a sign of danger in early 2159. For that reason he plans to leave the region before then. The Melnorme are friendly but insist on the rules of trade. If attacked, they fight back with a weapon system they bought from the Keel-Verezy, and they refuse to trade again until the player offers a sincere apology and pays reparations. Their catalog item 2418-B is the probe they sold to the Slylandro, which became the swarm of hostile red probes. In the Kohr-Ah history, a one-eyed race called the Mael-Num escaped the Kohr-Ah when the first Doctrinal War broke out. The dialogue never states outright that the Mael-Num are the Melnorme.

*Sources:* content/base/ships/melnorme/trader.txt, src/uqm/ships/melnorme/melnorme.c, src/uqm/element.h, doc/release/UQM-Manual.txt, content/base/comm/melnorme/melnorme.txt, content/base/comm/slylandro/slylandro.txt, content/base/comm/kohrah/kohrah.txt

---

## Mmrnmhrm

**Ship:** Mmrnmhrm X-Form · **Melee cost:** 19

"Transforms from a slow, heavy to a light, quick ship."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 10 |
| Energy regen | 2 per 6 frames |
| Max speed | 20 |
| Acceleration | 5 per 1 frames |
| Turn delay | 2 frames |
| Mass | 3 |
| Weapon / special cost | 1 / 10 (MAX_ENERGY) |

*Y-Form:* energy regen 1 per 6 frames, max speed 50, acceleration 10 per 0 frames, turn delay 14 frames, weapon cost 1 (weapon wait 20), transform cost 10. Crew, battery and mass are shared with the X-Form. In code, the Y-Form speed and acceleration are wrapped in RES_SCALE(). The X-Form values get the same scaling at load time.

**Primary:** Lasers (X-form) or homing missiles (Y-form).
**Secondary:** Switch between X-Form and Y-Form.

**Captains:** Qir-nha, Jhe-qir, Qua-rhna, Mn-quah, Nrna-mha, Um-hrh, Hm-nhuh, Rrma-hrn, Jra-nr, Ur-mfrs, Qua-qir, Mrm-na, Jhe-mhr, Hmr-hun, Nhuh-na, Hrnm-hm

### Lore

The Mmrnmhrm are a race of machines. Starbase records say a distant, unknown culture sent a giant Factory-Ark into this region centuries ago. Earth's press called it the "Mother-Ark". It built millions of robots and then broke down, and for unknown reasons the Mmrnmhrm never repaired it. Humans guess the robots are the vanguard of a colonization project. Before the war, the Mmrnmhrm once tried to colonize Beta Herculis. When the Spathi said the system was theirs, the Mmrnmhrm politely withdrew.

The Mmrnmhrm were core members of the Alliance of Free Stars, alongside the Chenjesu. A joint Mmrnmhrm and Chenjesu force turned the Ur-Quan back when the Ur-Quan attacked the Ilwrath. Later, the bulk of the Ilwrath fleet was thrown against those two races. In 2134 the Hierarchy concentrated its forces on Procyon, and the Ur-Quan finally brought the Sa-Matra into battle. The Chenjesu and Mmrnmhrm surrendered rather than be wiped out. Before the Ur-Quan arrived, they advised humanity to do the same. They chose to share a single slave shield on the Chenjesu homeworld at Procyon. Under it they are merging into one hybrid of crystalline and mechanical life, powered only by sunlight, a process expected to take about 35 years. They plan to break the shield when the process is done and destroy the Sa-Matra. They say more energy could speed the process up, but that this would be dangerous. The Mmrnmhrm have no dialogue file of their own. They speak only through the joint "we are the chenjesu... we are the mmrnmhrm" voice.

*Sources:* content/base/ships/mmrnmhrm/xform.txt, src/uqm/ships/mmrnmhrm/mmrnmhrm.c, doc/release/UQM-Manual.txt, content/base/comm/chmmr/chmmr.txt, content/base/comm/starbase/starbase.txt, content/base/comm/safeones/safeones.txt, content/base/comm/melnorme/melnorme.txt

---

## Mycon

**Ship:** Mycon Podship · **Melee cost:** 21

"Very slow. Homing plasma torpedo. Grows new crew."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 40 |
| Energy regen | 1 per 4 frames |
| Max speed | 27 |
| Acceleration | 9 per 6 frames |
| Turn delay | 6 frames |
| Mass | 7 |
| Weapon / special cost | 20 / 40 (MAX_ENERGY) |

**Primary:** Homing Plasmoid.
**Secondary:** Regenerate 4 crew.

**Captains:** Blort, Chupp, Floos, Glish, Glob, Glush, Plork, Shlish, Shlupp, Slingy, Sploozo, Spork, Uffo, Yush, Zaloop, Znuff

### Lore

The Mycon are a fungal species that thrive only at temperatures near the melting point of lead. They stand 0.5 to 3.5 metres tall. Their corpses have "a nasty habit of coming back to life" when thawed. They pass whole sets of memories to their offspring, so individual Mycon speak as long-dead ancestors and ramble about events from thousands of years ago. Examples are Dugee the purity monitor, who "died of general misfunction 57,283 years ago", Shloosh, and Gussh, who attends the birthing nodes. Everything they do serves Juffo-Wup, the spreading "hot light in the darkness" that must absorb or "Void" everything that is "Non". Its source lies at a fixed point in their space. Odd fragments in their speech ("planetary transformer biot 94-18", "when the Creators return") hint that they were engineered.

The Mycon colonize worlds with Deep Children. These are tough spore pods fired beneath a planet's crust that later burst out in huge calderas and fill the atmosphere with steam and sulphuric acid. This is how the "Shattered Worlds" are made, and the player can prove to the Syreen that it is how their homeworld Syra was destroyed. As far as humans know, the Mycon were the only race to actively seek out the Ur-Quan to become combat slaves. Their voluntary submission brought "a hundred devastating Mycon Podships" against the Alliance. While the Ur-Quan are distracted, the Mycon are expanding as fast as they can. A Shofixti scout saw them test a device at Beta Brahe that made a sun-like flare, and they later demand the "Solar Manipulator" back from the player. The player can lure their birthing fleet to a false colony world at Organon. They cannot really hold a conversation with humans, and they treat the player as Non to be removed.

*Sources:* content/base/ships/mycon/podship.txt, src/uqm/ships/mycon/mycon.c, doc/release/UQM-Manual.txt, content/base/comm/mycon/mycon.txt, content/base/comm/starbase/starbase.txt, content/base/comm/melnorme/melnorme.txt, content/base/comm/syreen/syreen.txt, content/base/comm/shofixti/shofixti.txt

---

## Orz

**Ship:** Orz Nemesis · **Melee cost:** 23

"Quick. Rotating turret. Space marines board enemy ship."

| Stat | Value |
|---|---|
| Crew (max) | 16 |
| Battery (max) | 20 |
| Energy regen | 1 per 6 frames |
| Max speed | 35 |
| Acceleration | 5 per 0 frames |
| Turn delay | 1 frames |
| Mass | 4 |
| Weapon / special cost | 6 (MAX_ENERGY / 3) / 0 |

**Primary:** Howitzer cannon.
**Secondary:** Secondary with left and right arrows rotates the primary cannon. Secondary with Primary launches space marines that invade the enemy ship and kill their crew.

**Captains:** \*Wet\*, \*Happy\*, \*Frumple\*, \*Camper\*, \*Loner\*, \*Dancer\*, \*Singer\*, \*Heavy\*, \*NewBoy\*, \*FatFun\*, \*Pepper\*, \*Hungry\*, \*Deep\*, \*Smell\*, \*Juice\*, \*Squirt\*

### Lore

The Orz arrived after the war, from somewhere "outside" or "below" normal space. Their speech comes through the ship's translator as a stream of starred words that don't quite fit ("*campers*", "*parties*", "*frumple*", "*squeezing the juice*"). The translator itself warns that the translation's accuracy is unknown. Each Orz insists "I am Orz. I do not have the name because I am Orz." They say what humans see as "*Orz bubbles*" are really the "*fingers*" of a single being, reaching into "*heavy space*". They could only "*smell*" this level of reality after the Androsynth's dimensional experiments opened "*slippery places*". The Orz dislike the Arilou, who also come from "outside" ("Orz are from *below*, Arilou are from *above*"). They also visit the Taalo "*Playground*", a world where the Taalo slid into "*Pretty Space*" to escape the Dnyarri.

According to the Melnorme, the Orz wiped out the Androsynth shortly after the war, "seemingly out of nowhere". Ask the Orz about the Androsynth often enough and they fly into a rage ("Nnnnggaaahhh!"), and pushing further turns them hostile. The Orz are keen to form an "*alliance*" with humans and will give them Nemesis ships with "GO! GO!" boarding marines. Their idea of alliance has an unsettling side: the Orz say humans will be "*pulled*", will "*become*", and will "*never leave*". They also speak of "*dissolving*" anyone who refuses to "*play*". The Orz homeworld is at Gamma Vulpeculae. The Orz name no individuals.

*Sources:* content/base/ships/orz/nemesis.txt, src/uqm/ships/orz/orz.c, doc/release/UQM-Manual.txt, content/base/comm/orz/orz.txt, content/base/comm/melnorme/melnorme.txt

---

## Pkunk

**Ship:** Pkunk Fury · **Melee cost:** 20

"Blazing fast. Insulting enemy. Chance of respawning"

| Stat | Value |
|---|---|
| Crew (max) | 8 |
| Battery (max) | 12 |
| Energy regen | 0 per 0 frames |
| Max speed | 64 |
| Acceleration | 16 per 0 frames |
| Turn delay | 0 frames |
| Mass | 1 |
| Weapon / special cost | 1 / 2 |

**Primary:** Three-way cannon.
**Secondary:** Fling insults at opponent. This is the only way the Pkunk can regenerate combat energy. (Note: on occasion, a destroyed Fury will be resurrected with full fuel and power.)

**Captains:** Awwky, Tweety, WudStok, Poppy, Brakky, Hooter, Buzzard, Polly, Ernie, Yompin, Fuzzy, Raven, Crow, Jay, Screech, Twitter

### Lore

The Pkunk are a birdlike, self-proclaimed psychic and spiritual race ("Hatchlings of light... birdlike manifestations of glorious light energies from the astral plane") whose name means "Peace". They are an offshoot of the Yehat that split from them early in the Yehat Space Age, once "brutal birds of prey" until Weeny Wikki Beeki Birdi gave the Original Squawk. They speak in New Age mysticism (past lives, crystal magic, Pyramid Power) and claim to love everyone, humans most of all. They explain that they hurl insults in battle because combat does not come easily to them, and they have to whip themselves into a frenzy to fight.

For about eight years the Pkunk have been under attack by the Ilwrath, who were set on them by a HyperWave broadcast supposedly from the Ilwrath gods Dogar and Kazon. The Pkunk later decide the gods are a hoax, having heard giggling at the end of a recording. Two-thirds of their civilization has been wiped out. Their homeworld is Gamma Krueger I. The Pkunk give the Captain the Precursor Clear Spindle and Fury starships, and through dreams and visions they hint at the other artifact pieces, the Kohr-Ah/Ur-Quan battle at Sa-Matra, and the Arilou. Their fleet keeps setting out to "reunite" with their Yehat siblings, who fire on Pkunk ships on sight. The Captain is asked to talk them out of it. Named Pkunk include the first officer Chrupp ("I don't think Chrupp likes you, Captain"), the elder Awkky Birdy, and the channeller Braky.

*Sources:* content/base/ships/pkunk/fury.txt, src/uqm/ships/pkunk/pkunk.c, doc/release/UQM-Manual.txt, content/base/comm/pkunk/pkunk.txt

---

## Shofixti

**Ship:** Shofixti Scout · **Melee cost:** 5

"Tiny, fast. Can self-destruct."

| Stat | Value |
|---|---|
| Crew (max) | 6 |
| Battery (max) | 4 |
| Energy regen | 1 per 9 frames |
| Max speed | 35 |
| Acceleration | 5 per 0 frames |
| Turn delay | 1 frames |
| Mass | 1 |
| Weapon / special cost | 1 / 0 |

**Primary:** Energy Dart.
**Secondary:** Glory Device. When pressed three times, the ship will self-destruct, inflicting vast damage on nearby vessels.

**Captains:** Hiyata, Wasabe, Kudzu, Ichiban, Bonsai!, Genjiro, Ginzu, Busu, Gaijin, Daikon, Sushi, Naninani, Chimchim, Tora-3, Tofu, Kimba, Tanaka, Katana

### Lore

The Shofixti are small, fierce, furry warriors who were uplifted by the Yehat a few decades before the war and fought for the Alliance of Free Stars. Their dialogue is a stream of creative insults ("Ur-Quan pus-cup", "pouchless lard-log freak") and battle cries ("Kyaiee!"). When the Ur-Quan's primary task force arrived at their homeworld, the Shofixti made their sun flare like a nova, which destroyed the system and hundreds of Hierarchy vessels. They believe this was the "ultimate sacrifice" that bought the Alliance's freedom.

The Captain meets Tanaka, a lone survivor guarding the dead home system. He mistakes the Captain's ship for an Ur-Quan vessel and attacks. Tanaka was away on a Yehat-squadron scouting mission at the time. At Beta Brahe he saw the Mycon test a small device that produced a flare "like a newborn sun", and on the way home he passed through a strange planet near Zeta Sextantis. A VUX Intruder's limpets slowed his ship, and his Glory Device switch broke. If Tanaka dies, his brother Katana comes home later and takes up the vigil. Once the Captain brings Shofixti females ("a bevy of fecund Shofixti nubiles"), the survivor sets about repopulating the species, and on later visits he complains about how exhausting it is. The Shofixti also revere the hero Daikon and wait for his return.

*Sources:* content/base/ships/shofixti/scout.txt, src/uqm/ships/shofixti/shofixti.c, doc/release/UQM-Manual.txt, content/base/comm/shofixti/shofixti.txt, content/base/comm/spathi/spathi.txt

---

## Slylandro

**Ship:** Slylandro Probe · **Melee cost:** 17

"Constant motion, instant reverse. Absorbs asteroids."

| Stat | Value |
|---|---|
| Crew (max) | 12 |
| Battery (max) | 20 |
| Energy regen | 0 per 10 frames |
| Max speed | 60 |
| Acceleration | 60 (= MAX_THRUST) per 0 frames |
| Turn delay | 0 frames |
| Mass | 1 |
| Weapon / special cost | 2 / 0 |

**Primary:** Lighting [sic] weapon.
**Secondary:** Absorb a nearby asteroid and convert to combat power. This is the only way the Probe can recharge. (Note: the Probe is inertia-less and always in motion. Pressing thrust will reverse its direction.)

**Captains:** 2418-B (all 16 captain entries are "2418-B")

### Lore

The Slylandro are "kind, curious gas bag people" who live in a 500 km band of atmosphere on the gas giant they call Source. They have no physical technology and cannot leave their world, so they depend on rare visitors for news of the galaxy. They keep time in Drahn (four million planetary rotations) and record their history in History Chants. The Captain talks with the Speaker Content To Hover, along with the associates Joyous Lifting and Sullen Plummet. They remember visits from the Sentient Milieu (Yuli, Drall, Taalo, Mael-Num, Faz and the Ur-Quan, who were then "long brownish guys" and "really nice"). They also remember the "Shaggy Ones", apparently the Precursors, who left a broadcasting satellite in orbit and told them of ten special worlds.

The Melnorme traded them catalog item 2418, a Remote Self-Replicating Robot Explorer Probe ("the economy model"), for data on Source's life. Joyous Lifting raised the probe's replication priority from 2 to 999. As a result, once a probe finishes contacting a ship, it treats that ship as raw material and breaks it apart with its electrical discharge device. The Slylandro insist the probe is armed only with defensive missiles. The probes themselves (designation "2418-B") broadcast endless peaceful greetings in all caps ("WE COME IN PEACE") and then attack. When the Captain explains what went wrong, the Slylandro are horrified and give up a self-destruct code. Later they reconfigure a returning probe to hunt down the others and broadcast that code.

*Sources:* content/base/ships/slylandro/probe.txt, src/uqm/ships/slylandr/slylandr.c, doc/release/UQM-Manual.txt, content/base/comm/slylandro/slylandro.txt, content/base/comm/probe/probe.txt

---

## Spathi

**Ship:** Spathi Eluder · **Melee cost:** 18

"Very fast. Large, cowardly crew. Rear firing weapon."

| Stat | Value |
|---|---|
| Crew (max) | 30 |
| Battery (max) | 10 |
| Energy regen | 1 per 10 frames |
| Max speed | 48 |
| Acceleration | 12 per 1 frames |
| Turn delay | 1 frames |
| Mass | 5 |
| Weapon / special cost | 2 / 3 |

**Primary:** Simple forward cannon.
**Secondary:** Backward Utilized Tracking Torpedo (B.U.T.T.), a homing missile fired from the rear of the vessel.

**Captains:** Thwil, Pwappy, Phwiff, Wiffy, Plibnik, Snurfel, Kwimp, Pkunky, Jinkeze, Thintho, Rupatup, Nargle, Phlendo, Snelopy, Bwinkin, Whuff, Fwiffo

### Lore

The Spathi are one-eyed "Meta-Mollusks" who openly admit to being cowards ("Yes, absolutely, and with no qualifications"). Their daily prayer is "Oh God... Please don't let me die today! Tomorrow would be so much better!" Their homeworld Spathiwa orbits the orange giant Yuffo, and they fear an unseen "Ultimate Evil". After the Ur-Quan crushed the Ilwrath, they subjugated the Spathi. The Spathi leaders meant to choose fallow slavery, but an Umgah servant swapped the white rod for the black one, and the Spathi became combat thralls of the Hierarchy by mistake.

The Spathi and Ilwrath were posted to the Earthguard to watch over the slave-shielded humans. The Ilwrath left, and the nervous Spathi "strategically redeployed" from Luna to Mars, Ganymede, Titan and finally Pluto. They left androids pushing dirt around on Luna and a radio playing the FunRom "Winky's Happy Night". They also sent their ships home one at a time by the Puun-Taffy ritual, until only Captain Fwiffo of the voidship StarRunner was left, alone on Pluto. Fwiffo is the first alien the Captain meets. He blurts out his homeworld's coordinates and the "ultra-secret" Spathi cypher at once, and he can be persuaded to join the fleet. He fills the Captain in on the war and the Earthguard and tells his own life story: youngest of 18,487 siblings, knocked out by a vegetable cart, and conscripted into the navy. For anything beyond that, he points the Captain to the High Ruling Council at Spathiwa.

*Sources:* content/base/ships/spathi/eluder.txt, src/uqm/ships/spathi/spathi.c, doc/release/UQM-Manual.txt, content/base/comm/spathi/spathi.txt

---

## Supox

**Ship:** Supox Blade · **Melee cost:** 16

"Light. Rapid-fire globs. Slides in any direction."

| Stat | Value |
|---|---|
| Crew (max) | 12 |
| Battery (max) | 16 |
| Energy regen | 1 per 4 frames |
| Max speed | 40 |
| Acceleration | 8 per 0 frames |
| Turn delay | 1 frames |
| Mass | 4 |
| Weapon / special cost | 1 / 1 |

**Primary:** Forward firing glob weapon.
**Secondary:** Secondary + left or right will cause you to drift laterally, while Secondary + thrust will make you fly backwards. This cancels your current velocity, so be careful!

**Captains:** Trifid, Crinoid, FlyTrap, Thistle, Ivy, Sprout, Twig, Root, Branch, Thorn, Bark, Bud, Nut, Stem, Bramble, Thicket

### Lore

The Supox are intelligent, symbiotic plants from a world orbiting the green star Root. They evolved alongside hardier species, trading reproductive help for nutrients. Their "first step in making friends is always to copy them", so at first contact they mirror the Captain's words back ("I am Captain Ala-la'la... Our starship is called the Tender Shoot... We are the Supox Utricularia from Earth"). They greet in plant idioms ("may your roots always be well watered") and are close friends and allies of the Utwig, whom they follow in all things.

The Supox hand the Captain the broken Ultron, a junk artifact the Druuge sold to the Utwig. Its loss has left the Utwig depressed, and the Supox ask the Captain to repair it. Later they fight the Kohr-Ah at the Utwig's side, targeting only the Kohr-Ah so the two Ur-Quan factions stay evenly matched, even though the Ur-Quan keep firing on them. They pass on the intercepted "Sa-Matra" signal and tell of a strange sensor-scrambling world at Beta Leporis. They can send a pod of Blades to join the Captain's fleet.

*Sources:* content/base/ships/supox/blade.txt, src/uqm/ships/supox/supox.c, doc/release/UQM-Manual.txt, content/base/comm/supox/supox.txt

---

## Syreen

**Ship:** Syreen Penetrator · **Melee cost:** 13

"Lithe space vixens who steal enemy's crew."

| Stat | Value |
|---|---|
| Crew (max) | 12 (ship can hold up to 42 via SYREEN_MAX_CREW_SIZE) |
| Battery (max) | 16 |
| Energy regen | 1 per 6 frames |
| Max speed | 36 |
| Acceleration | 9 per 1 frames |
| Turn delay | 1 frames |
| Mass | 2 |
| Weapon / special cost | 1 / 5 |

**Primary:** Particle Beam Stiletto.
**Secondary:** "Syreen Call", a psychic attack that induces enemy crew to jump ship, where you (or your opponent) may capture them to add to your complement.

**Captains:** Teela, Dejah, Penny, Alia, Be'lit, Ripley, Yarr, Ardala, Sparta, Munro, Danning, Brawne, Maya, Aelita, Alura, Dale

### Lore

The Syreen are a humanoid race almost identical to humans ("Except for... certain parts..."). Their culture parallels Earth's but split from it around 5000 BCE, when their farming peoples were never conquered by herding tribes. Their homeworld Syra (Beta Copernicus I) was destroyed after an "asteroid" punched into its mantle and calderas later opened across the whole planet. The survivors were mostly from the largely female Space Patrol: fewer than ten thousand people, only five hundred of them male. They spent 75 years wandering at sub-light speed in makeshift Habitat ships. They joined the Alliance only out of necessity, since the VUX were raiding their Habitats. When Earth fell and the Alliance broke apart, they surrendered and became fallow slaves on Gaia, a world the Ur-Quan Master Nine found for them.

Starbase Commander Talana, who lost her sister Diani at Raynet, refuses at first to risk Gaia. When the Captain brings proof that Mycon Deep Children destroyed Syra, she swears revenge. The Captain then recovers the Syreen Penetrator fleet from an Ur-Quan vault on the moon of Epsilon Camelopardalis I. Next he lures the Mycon to the blue world at Organon, where the Syreen ambush and wreck their fleet. Afterward the Syreen give the Captain their officers and Penetrator designs. Talana flirts with the Captain throughout and can become his lover.

*Sources:* content/base/ships/syreen/penetrator.txt, src/uqm/ships/syreen/syreen.c, doc/release/UQM-Manual.txt, content/base/comm/syreen/syreen.txt

---

## Thraddash

**Ship:** Thraddash Torch · **Melee cost:** 10

"Nimble. Afterburner accelerates ship, burns enemy."

| Stat | Value |
|---|---|
| Crew (max) | 8 |
| Battery (max) | 24 |
| Energy regen | 1 per 6 frames |
| Max speed | 28 |
| Acceleration | 7 per 0 frames |
| Turn delay | 1 frames |
| Mass | 7 |
| Weapon / special cost | 2 / 1 |

**Primary:** Straightforward blaster cannon.
**Secondary:** Afterburner. The afterburner exhaust does more damage than the blaster, so use it as a weapon.

**Captains:** Dthunk, Bardat, Znonk, Mnump, Bronk, Smup, Grulk, Hornk, Knarg, Drulg, Dgako, Znork, Kwamp, Fkank, Pdump, Whumps

### Lore

The Thraddash are loud, snorting "Rhino-Dudes" who believe a good fight is the only way to learn and improve. Their history is a string of violent "Cultures", each of which overthrew the one before it. The current one is Culture Nineteen. Their stories include Culture Three, who cut off their own limbs to scare enemies, and peaceful Culture Fourteen, who were conquered after only ten years, which the Thraddash treat as "proof" that peace fails. Their most sacred relic is the Aqua Helix, kept in a shrine on the dark continent of Funt. Every Culture has held it as the sign of its authority.

The Ur-Quan arrived from the direction of Ophiuchi more than fifty years ago and defeated them quickly. The Thraddash call themselves the first and finest Ur-Quan combat thralls. The Ur-Quan disagreed: they judged them too weak and too troublesome, partly because they kept picking fights with newer thralls like the Umgah and Ilwrath. So the Thraddash were left behind to guard the flank and never fought the Alliance. Maintenance engineer Reeunk invented their signature afterburner in 2143 when he stuck his cigar in a fuel valve, which killed him. The Captain can talk them into attacking the Kohr-Ah ("the dark ships") to impress the Ur-Quan. They lose over half their fleet, about 40% of it to the Ur-Quan themselves.

The Thraddash despise humans as weaklings, but a Captain who beats them enough times becomes their revered "Great Teacher". They then clumsily try out new greetings on the Captain's advice (courtesy, rhyming, pig latin) and can found a Culture Twenty. Named speakers include Korgk, battle-slave foreman of Culture Nineteen; Commander Dthunk of the starship *Overwhelmer*; Grah of the *Hot Pulsing Thrusters*; and Captain Chudd of the *Blazing Guns of Glory*.

*Sources:* content/base/ships/thraddash/torch.txt, src/uqm/ships/thradd/thradd.c, doc/release/UQM-Manual.txt, content/base/comm/thraddash/thraddash.txt

---

## Umgah

**Ship:** Umgah Drone · **Melee cost:** 7

"Stubby and slow. Anti-matter cone. Zips backwards."

| Stat | Value |
|---|---|
| Crew (max) | 10 |
| Battery (max) | 30 |
| Energy regen | 30 (= MAX_ENERGY) per 150 frames |
| Max speed | 18 |
| Acceleration | 6 per 3 frames |
| Turn delay | 4 frames |
| Mass | 1 |
| Weapon / special cost | 0 / 1 |

**Primary:** Anti-matter cone. Does not require combat batteries to use.
**Secondary:** Fly backwards suddenly and at high speed.
*Note:* The Drone only recharges its batteries if you do not fire for a long time, and then all the energy returns in one lump.

**Captains:** Julg'ka, Gibj'o, Baguk'i, O'guk'e, Gwap'he, Chez'ef, Znork'i, Bob, Kwik'ow, Ei'Ei'o, Brewz'k, Pruk'u, O'bargy, Kterbi'a, Chup'he, I'buba

### Lore

The Umgah are blob-like "crazy blobbies" and Ur-Quan battle thralls. They are obsessed with practical jokes and have little regard for anyone they play them on. They are also masters of biotechnology: their homeworld has "nothing but vast supply of biological skills and data". As a reward they offer to graft extra eyes and tentacles onto the Captain. Their past pranks include the "Dogar and Kazon" routine they pulled on the Ilwrath, which ended when the Spathi stole their HyperWave 'Caster. They once kidnapped a Mycon to dissect it and found that the Mycon are artificial constructs, not products of evolution.

The Arilou brought the Umgah an injured creature, the Talking Pet, which they had found in the wreck of an Ur-Quan Dreadnought. The Umgah healed it and boosted its intelligence with genetic changes, intending to have it issue fake Ur-Quan orders (such as ordering the Spathi to attack the VUX). Within hours of waking, the creature took mental control of the hospital, then the city, then the whole planet. During the game the Umgah talk in a flat, robotic monotone ("HUMAN. MUST. BE. ELIMINATED.") while serving its "Big Plan" of revenge against the Ur-Quan. Once the Captain deals with the Talking Pet, the Umgah hail them as a hero and hand over Biological Data. They soon get bored of that and declare the Captain their "Great Enemy" for fun. Officer Flubbo is mentioned by name.

*Sources:* content/base/ships/umgah/drone.txt, src/uqm/ships/umgah/umgah.c, doc/release/UQM-Manual.txt, content/base/comm/umgah/umgah.txt

---

## Ur-Quan (Kzer-Za)

**Ship:** Ur-Quan Dreadnought · **Melee cost:** 30

"Huge, slow. Heavy weapon. Launches fighters."

| Stat | Value |
|---|---|
| Crew (max) | 42 (MAX_CREW_SIZE) |
| Battery (max) | 42 (MAX_ENERGY_SIZE) |
| Energy regen | 1 per 4 frames |
| Max speed | 30 |
| Acceleration | 6 per 6 frames |
| Turn delay | 4 frames |
| Mass | 10 |
| Weapon / special cost | 6 / 8 |

**Primary:** Fusion Blast.
**Secondary:** Launches autonomous fighters to harass the enemy. When their fuel runs low they fly back to the Dreadnought, so catch them before they expire. Each fighter needs one crew member to pilot it, so take care not to weaken the core ship.

**Captains:** Lord 999, Lord 342, Lord 88, Lord 156, Lord 43, Lord 412, Lord 666, Lord 18, Lord 237, Lord 89, Lord 3, Lord 476, Lord 103, Lord 783, Lord 52, Lord 21

### Lore

The Kzer-Za are the green Ur-Quan, masters of the Hierarchy that defeated the Alliance of Free Stars and placed Earth under a slave shield. If the Captain speaks "the Words", they explain why. The Ur-Quan descend from solitary hunters on a hostile world. They joined the six races of the Sentient Milieu, until a scoutship met the Dnyarri, mind-controlling creatures who enslaved them for thousands of years. The Dnyarri engineered the Ur-Quan into two sub-races: the Green thinkers and planners, and the Black warriors and laborers. The "martyred genius" Kzer-Za found the secret to defeating the Dnyarri, and afterwards the Ur-Quan vowed never to be slaves again. They took up the Path of Now and Forever: enslave or imprison all other intelligent life.

The Black Ur-Quan, under Kohr-Ah, adopted the Eternal Doctrine of exterminating all non-Ur-Quan life. They burned the Yuptar homeworld before the Kzer-Za defeated them and exiled them, and the two factions then moved around the galaxy in opposite directions. The game takes place during their latest Doctrinal War. The two sides fight for the Sa-Matra, the ancient symbol of Ur-Quan dominance, and the winner's doctrine prevails. The Kzer-Za insist they never lie, that slavery is a "boon" that protects species from themselves, and that they have saved hundreds of species from extinction over twenty thousand years.

The Kzer-Za react with horror to news of a mind-controlling Talking Pet, a "neo-Dnyarri" in Umgah space. They release the Captain and vow to deal with it once the Kohr-Ah are beaten. If the Kohr-Ah win, the defeated Kzer-Za urge the humans to flee and hide while they themselves stay to guard the Sa-Matra. Their Dreadnought commanders carry numbered titles (Lord 999, Lord 342, and so on). In a hidden gag, the small translator figure in the corner of the comm screen speaks for himself and wishes the game had been a musical.

*Sources:* content/base/ships/urquan/dreadnought.txt, src/uqm/ships/urquan/urquan.c, src/uqm/element.h, doc/release/UQM-Manual.txt, content/base/comm/urquan/urquan.txt

---

## Utwig

**Ship:** Utwig Jugger · **Melee cost:** 22

"Weapons consume no energy. Absorbent shields."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 20 |
| Energy regen | 0 per 255 frames |
| Max speed | 36 |
| Acceleration | 6 per 6 frames |
| Turn delay | 1 frames |
| Mass | 8 |
| Weapon / special cost | 0 / 1 |

**Primary:** Six-shot cannon. Requires no combat battery energy to fire.
**Secondary:** Force shield. Absorbing hits re-energizes your batteries. When the batteries are exhausted, the shield is permanently disabled until combat ends.

**Captains:** Endo, Vermi, Manny, Uuter, Nergo, Sami, Duna, Frann, Krisk, Lololo, Snoon, Nestor, Lurg, Thory, Jujuby, Erog, Tarp

### Lore

The Utwig are a masked species from the world Fahz, governed by the Utwig Proctorate. In their primitive past "the veils fell": they realized that the face shows the primitive urges (greed, rage, hatred, lust) that hold back sentience. Since then they have covered their faces, and over the generations they built an elaborate etiquette of masks for every occasion, from the Mask of Grueling but Necessary Activity to the Countenance of Stellar Representation.

Their society centered on the Ultron, a device the Druuge had delivered to them, which "assured total and complete meaning of life for All". During the Chinz-Rahl celebration the Grand Proctor handed it to the Chief Groo, who dropped it, and it broke. In shame the Utwig burned every mask except the Mask of Ultimate Embarrassment and Shame, and gave the husk to their allies, the Supox. They now live in collective depression. They keep a Precursor planet-cracking "Bomb" on the second moon of the sixth planet of Zeta Hyades in case they decide to end their existence.

The Utwig took no part in the Alliance–Hierarchy war and know nothing of the Ur-Quan. They did skirmish with the Kohr-Ah, and found their absorbing shields could sweep through the spinning blades and soak up the fiery corona. When the Captain restores the Ultron, the Utwig and Supox join the Captain's new alliance, supply ships and trained commanders, and launch an offensive against the Kohr-Ah only. The Ultron also tells them the Bomb must be "improved" to fulfill its final destiny.

*Sources:* content/base/ships/utwig/jugger.txt, src/uqm/ships/utwig/utwig.c, doc/release/UQM-Manual.txt, content/base/comm/utwig/utwig.txt

---

## VUX

**Ship:** VUX Intruder · **Melee cost:** 12

"Clumsy. Powerful laser. Spawns limpet parasites."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 40 |
| Energy regen | 1 per 8 frames |
| Max speed | 21 |
| Acceleration | 7 per 4 frames |
| Turn delay | 6 frames |
| Mass | 6 |
| Weapon / special cost | 1 / 2 |

**Primary:** Gigawatt laser.
**Secondary:** Limpet mines that track enemy ships and slow them down dramatically if they hit.

**Captains:** ZIK, PUZ, ZUK, VIP, ZIT, YUK, DAK, ZRN, PIF, FIZ, FUP, ZUP, NRF, ZOG, ORZ, ZEK

### Lore

The VUX are one-eyed, chitinous Ur-Quan Hierarchy thralls who find humans physically revolting. Talking to a human makes them want to vomit, and they insult humans constantly ("two-eyed loathsome faceless slug"). They officially blame the First Human Encounter, when a Captain Rand insulted a VUX starship commander. If the Captain apologizes enough times, they finally admit the real reason: humans are simply too ugly for them to bear. They say they attack because the Ur-Quan wish it. VUX Commander YAX is one of the taunting speakers.

The exception is Admiral ZEX (called General ZEX by the Yehat), who commanded the entire VUX fleet during the war against the Alliance. The Yehat rebels call him a genuine genius. He invented the tactics of Fortress Square and the Dynamic Triangle, and without him the VUX would have fallen in weeks. Disgusted by his "perverted" fondness for humans, the Primat and the VUX High Council sent him into a hero's exile at Alpha Cerenkov I. There he keeps a menagerie of "beautiful" (to VUX, hideous) creatures and holds the Shofixti Maidens. He offers to trade the Maidens for a beast from Delta Lyncis, then tries to add the Captain to his collection. The beast escapes, kills him, and leaves Sub-commander DAX in charge. He also bluffs about owning a Precursor warp nullifier.

*Sources:* content/base/ships/vux/intruder.txt, src/uqm/ships/vux/vux.c, doc/release/UQM-Manual.txt, content/base/comm/vux/vux.txt, content/base/comm/yehatrebels/yehatrebels.txt

---

## Yehat

**Ship:** Yehat Terminator · **Melee cost:** 23

"Agile. Rapid-fire, twin missiles. Shield."

| Stat | Value |
|---|---|
| Crew (max) | 20 |
| Battery (max) | 10 |
| Energy regen | 2 per 6 frames |
| Max speed | 30 |
| Acceleration | 6 per 2 frames |
| Turn delay | 2 frames |
| Mass | 3 |
| Weapon / special cost | 1 / 3 |

**Primary:** Twin autocannons.
**Secondary:** Force shield.

**Captains:** Heep-eep, Feep-eep, Reep-eep, Yeep-eep, Beep-eep, Eeep-eep, Meep-eep, Teep-eep, Jeep-eep, Leep-eep, Peep-eep, Weep-eep, Veep-eep, Geep-eep, Zeep-eep, Neep-eep

### Lore

The Yehat are proud, honor-bound "birds of prey" with a burr in their speech ("ye", "yer"). Long ago they were barbarous warring Clans, until the first Veep-Neep Queen united them from the High Perch of Caer Zeep-Reep. In exchange for the Clans' fealty, she promised they would never suffer defeat, and her dynasty kept that promise for more than two thousand years. The Yehat fought in the Alliance of Free Stars beside humans and their "adopted children", the Shofixti, and earlier waged a Great War against the Mycon. When the Ur-Quan reached the Yehat home system at Gamma Serpentis, the current Queen allied with them rather than fight, keeping the "never defeated" promise in name only. She ordered the fleet to abandon the Shofixti at Delta Gorno. The Shofixti then detonated a Precursor device in their own sun, destroying nearly thirty percent of the Hierarchy fleet. The Yehat insist they are "Battle Thralls", not slaves.

The Starship Clans are ashamed and sympathetic to humans, but stay loyal to the Queen. The Pkunk are a cowardly offshoot whom the Yehat let leave the Nest a thousand years ago and now consider a deep embarrassment. When the Captain shows them a living Shofixti, the Zeep-Zeep Clan declares the Queen dishonored and starts a revolution, renewing the Wars of Ascension. The Royalist Feep-Eeep Clan wants the Captain dead. The rebels, led by Cheep-Guava and later joined by the Veep-Kreep Clan, supply Terminators and tell the Captain the Sa-Matra is the Hierarchy's weak point. If the rebellion succeeds, they crown a Pkunk, Braky Girdy the First, as the new Queen and send Terminators and Pkunk Furies to join the attack on the Sa-Matra.

*Sources:* content/base/ships/yehat/terminator.txt, src/uqm/ships/yehat/yehat.c, doc/release/UQM-Manual.txt, content/base/comm/yehat/yehat.txt, content/base/comm/yehatrebels/yehatrebels.txt

---

## Zoq-Fot-Pik

**Ship:** Zoq-Fot-Pik Stinger · **Melee cost:** 6

"Small crew. Speedy. Anti-matter spray, tongue attack."

| Stat | Value |
|---|---|
| Crew (max) | 10 |
| Battery (max) | 10 |
| Energy regen | 1 per 4 frames |
| Max speed | 40 |
| Acceleration | 10 per 0 frames |
| Turn delay | 1 frames |
| Mass | 5 |
| Weapon / special cost | 1 / 7 (MAX_ENERGY * 3 / 4) |

**Primary:** Anti-matter spray gun.
**Secondary:** "Tongue attack", a point-blank range attack that does grievous damage.

**Captains:** NikNak, FipPat, DipPak, FatPot, ZikFat, PukYor, TopNik, PorKoo, TikTak, RinTin, FitFap, TotToe, ZipZak, TikTok, MikMok, SikSok

### Lore

The Zoq-Fot-Pik are a cooperative union of three species, the Zoq, the Fot, and the Pik, who evolved intelligence on the same world at the same time as a fourth species, the predatory Zebranky. The Zebranky ate the other three, so the three banded together and wiped them out. They then spent about five thousand years enjoying the forest. Progress began when a lightning-cut, burning stone disk rolled down a hill and killed a Zoq, and the survivors discovered the Wheel, Fire, and Religion all at once. Their emissaries always talk in pairs: one is earnest and friendly, the other is suspicious and contrary. They endlessly argue over which of them is "the Fot", and one keeps bringing up Frungy, "the Sport of Kings".

The Zoq-Fot-Pik were not part of the original war. They knew of the "fabled" Alliance of Free Stars through the Chenjesu ("the great Crystal ones"), who had promised them help. Their colonies were destroyed by stray fire from the Doctrinal War between green fighter-launching battleships (the Ur-Quan) and black ships with alien writing on their hulls (the Kohr-Ah), which fight near gravity wells. The warring fleets have found only their colonies, not their homeworld, the planet closest to the sun at Alpha Tucanae. They offer a mutual-assistance pact, providing captains and Stinger designs in exchange for protection. Later they become a scouting ally, reporting on the Ur-Quan/Kohr-Ah war and warning that the Kohr-Ah will probably win. A lone Kohr-Ah ship may attack their homeworld, which survives only by focusing its planetary shields.

*Sources:* content/base/ships/zoqfotpik/stinger.txt, src/uqm/ships/zoqfot/zoqfot.c, doc/release/UQM-Manual.txt, content/base/comm/zoqfotpik/zoqfotpik.txt
