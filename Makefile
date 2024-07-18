fname = new_$(shell date +'%Y%m%d%H%M').md

.PHONY: serve
serve:
	hugo server -D

.PHONY: new
new:
	hugo new posts/${fname}
	nvim content/posts/${fname}
