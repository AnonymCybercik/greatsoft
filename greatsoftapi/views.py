from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view
from .models import Blog,Portfolio,Contact

@api_view(["GET"])
def OverAll(request):

    api_url = {

        "Blog Create":"api/Blog-Create",
        "Blog Update":"api/Blog-Update",
        "Blog Detail":"api/Blog-Detail/pk",
        "Blog Delate":"api/Blog-Delete/pk",
        "-----------":"----------------",
        "Portfolio Create":"api/Portfolio-Create",
        "Portfolio Update":"api/Portfolio-Update",
        "Portfolio Detail":"api/Portfolio-Detail/pk",
        "Portfolio Delate":"api/Portfolio-Delete/pk",
        "----------------":"---------------------",
        "Contact Create":"api/Contact-Create",
        "Contact Update":"api/Contact-Update",
        "Contact Detail":"api/Contact-Detail/pk",
        "Contact Delate":"api/Contact-Delete/pk",
    }

    return Response(data = api_url)

# # # # # # # # # # END OverALL

# # # # # # # # # # BLOG API # # # # # # # # # #

@api_view(['GET'])
def BlogList(request):
	blogs = Blog.objects.all().order_by('-id')
	serializer = BlogSerializer(blogs, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def BlogDetail(request, pk):
	blogs = Blog.objects.get(id=pk)
	serializer = BlogSerializer(blogs, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def BlogCreate(request):
	serializer = BlogSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def BlogUpdate(request, pk):
	blog = Blog.objects.get(id=pk)
	serializer = BlogSerializer(instance=blog, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def BlogDelete(request, pk):
	blog = Blog.objects.get(id=pk)
	blog.delete()

	return Response('Blog succsesfully delete!')

# # # # # # # END BLOG API # # # # # #

#######################################

# # # # # # # PORTFOLIO API # # # # # #

@api_view(['GET'])
def PortfolioList(request):
	portfolios = Portfolio.objects.all().order_by('-id')
	serializer = PortfolioSerializer(portfolios, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def PortfolioDetail(request, pk):
	portfolios = Portfolio.objects.get(id=pk)
	serializer = PortfolioSerializer(portfolios, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def PortfolioCreate(request):
	serializer = PortfolioSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def PortfolioUpdate(request, pk):
	portfolio = Portfolio.objects.get(id=pk)
	serializer = PortfolioSerializer(instance=portfolio, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def PortfolioDelete(request, pk):
	portfolio = Portfolio.objects.get(id=pk)
	portfolio.delete()

	return Response('Portfolio succsesfully delete!')

# # # # # # # END PORTFOLIO API # # # # # #

#######################################

# # # # # # # CONTACT API # # # # # #

@api_view(['GET'])
def ContactList(request):
	contacts = Contact.objects.all().order_by('-id')
	serializer = ContactSerializer(contacts, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def ContactDetail(request, pk):
	contacts = Contact.objects.get(id=pk)
	serializer = ContactSerializer(contacts, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def ContactCreate(request):
	serializer = ContactSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def ContactUpdate(request, pk):
	contact = Contact.objects.get(id=pk)
	serializer = ContactSerializer(instance=contact, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def ContactDelete(request, pk):
	contact = Contact.objects.get(id=pk)
	contact.delete()

	return Response('Contact succsesfully delete!')


# # # # # # # END CONTACT API # # # # # #
