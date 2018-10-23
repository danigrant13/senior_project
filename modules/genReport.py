

def run(context):
    reportName = "ppt_{}.csv".format(context['options']['subject'])
    report = context['report']

    data = [str(info) for info in report['data']]

    f = open(reportName, 'w')
    f.write(",".join(report['headers']) + "\n")
    f.write(",".join(data) + "\n")

    return context
