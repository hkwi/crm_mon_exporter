import flask
import subprocess
import lxml.etree

def safe_label(name):
	return name.replace("-","_").replace(".","_")

def collect():
	values = ""
	current = {}
	x = subprocess.check_output(["crm_mon","-X"])
	t = lxml.etree.fromstring(x)
	for n in t.xpath("./nodes/node"):
		txt = "crm_mon_nodes{%s} %d\r\n" % (
			",".join(['%s="%s"' % (k,v) for k,v in n.attrib.items()]),
			int(n.attrib.get("resources_running","0")),
		)
		values += txt
		
		name = n.attrib.get("name", "-")
		if n.attrib.get("is_dc")=="true":
			current[name] = 1
		elif n.attrib.get("is_dc")=="false":
			current[name] = 0
	
	values += "crm_mon_current_dc{%s} 1\r\n" % (
		",".join(['%s="%d"' % (safe_label(k), v) for k,v in current.items()]),
	)
	
	for g in t.xpath(".//resources/group"):
		for r in g.xpath(".//resource"):
			for n in r.xpath(".//node"):
				data={k:v for k,v in r.attrib.items()}
				data.update({"node_"+k:v for k,v in n.attrib.items()})
				data.update({"group_"+k:v for k,v in g.attrib.items()})
				
				txt = "crm_mon_resource{%s} 1\r\n" % (
					",".join(['%s="%s"' % (k,v) for k,v in data.items()]),
				)
				values += txt
	
	return values

app = flask.Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():
	return collect()

def cli():
	print(collect())

if __name__=="__main__":
	cli()
