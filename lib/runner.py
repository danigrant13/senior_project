def go(modules, initialContext={}):
    context = initialContext
    for mod in modules:
        context = mod.run(context)
    return context
