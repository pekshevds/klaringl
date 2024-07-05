from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import View
from index_app.models import (
    Const
)
from branch_app.models import Branch


class BranchOfficesView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "const": Const.info(),
            "items": Branch.active_branchs()
        }
        return render(request,
                      "branch_app/index.html",
                      context)
