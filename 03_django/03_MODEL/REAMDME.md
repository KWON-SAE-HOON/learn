# Project : Model

## App name : blog

## blog - Model

- `Article`
    - `title` : `CharField(200)`
    - `content` : `TextField()`
    - `created_at` : `DateTimeField()`
    - `updated_at` : `DateTimeField()`



## blog - URL conf
> Uniformed Resource Locator
- `blog//new/` 
    - 사용자에게 글을 작성하는 HTML을 제공
    - `new.html`
- `blog/create`
    - 사용자가 POST로 보낸 데이터를 저장
    - ???
- `blog/`
    - 전체 게시글(article)을 조회하는 HTML 제공
    - 게시글은 제목만 표시하며, 링크로 구성한다
    - `index.html`
- `blog/1/`
    - 특성 게시글을 조회하는 HTML 제공
    - 게시글의 제목/내용/작성시간/수정시간을 보여준다.
    - `detail.html`
- `blog/1/edit/`
    - 특정 게시글을 수정하도록 form을 보여주는 HTML 제공
    - `edit.html`
- `blog/1/update/`
    - 사용자가 Form을 통해 제출한 데이토로 게시글을 수정
    - ?????
- `blog/1/delete`
    - 특정 게시글을 삭제
    - 목록페이지로 redirect


사용자가 블로깅을 하는거
블로깅 => 글을 CRUD

1. 사용자가 ~ URL에 접속함
2. 게시글을 입력하는 HTML (form) 이 나옴
3. 사용자가 글을 쓰고 전송(Post)함
4. View 함수에서 Model과 통신하여 글을 저장함
5. 사용자에게 ~~한 Res 보내준다