import os
import sys

github_token = os.environ.get("GITHUB_TOKEN")
if github_token:
    print(f"GitHub 토큰이 설정되었습니다: {github_token[:4]}...{github_token[-4:]}")
else:
    print("GitHub 토큰이 설정되지 않았습니다.")
    sys.exit(1)

print("토큰 확인 완료!") 