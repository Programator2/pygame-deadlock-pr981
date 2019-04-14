This repo contains scripts to reproduce deadlocks occurring in pygame v1.9.5 music module. There is one script for each method:

* music.get_busy()
* music.rewind()
* music.set_pos()
* music.set_volume()

It shouldn't take longer than a minute for deadlock to occur. Otherwise, tweak the sleeping times.

---

> Music by Carl Larsson (aka Nightbeat), sound effect from PySolFC.
