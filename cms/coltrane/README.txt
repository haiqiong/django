Author: haiqiong yao
date: 6/13/2012

weblog app

1. build Entry model and Category model.
(1) add Categories and Enties to admin interface.
(2) date + slug = URL of each entry
(3) choices (enumerate)
(4) Tagging need to apply to Entry and Link models.
django-tagging to deal with generic relation.
(5) markdown converts text to html
(6) get_object_or_404(model, conditions)
(7) generic views: doesn't work
(8) decoupling the URLs by include()
the decorator, permalink(), doesn't work.
The layout of path is hard-code in get_absolute_url()

2. Link model
(1) the add() of PyDelicious module doesn't work.
(2) not complete for generic views.

3. Template


