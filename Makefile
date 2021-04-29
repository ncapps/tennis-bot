.PHONY: get-secret update-secret

_PWD = $(shell pwd)
_MKDIR = $(shell mkdir -p)
SECRET_ID = court_reserve_secret
DOWNLOADS_PATH = $(_PWD)/downloads
SECRET_FILE = $(DOWNLOADS_PATH)/config.json

$(shell mkdir -p $(DOWNLOADS_PATH))

get-secret:
	@echo "Downloading secret..."
	@aws secretsmanager get-secret-value --secret-id $(SECRET_ID) | jq -r .SecretString > $(SECRET_FILE)

update-secret:
	@echo "Updating secret in Secrets Manager"
	@aws secretsmanager update-secret --secret-id $(SECRET_ID) --secret-string file://$(SECRET_FILE)

clean:
	@echo "Cleaning..."
	@-rm -rf $(DOWNLOADS_PATH)

$(DOWNLOADS_PATH):
	mkdir -p $@