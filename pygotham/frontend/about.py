"""About PyGotham."""

from flask import Blueprint, render_template

from pygotham.models import AboutPage

__all__ = ('blueprint',)

blueprint = Blueprint(
    'about',
    __name__,
    subdomain='<event_slug>',
    url_prefix='/about',
)


@blueprint.route('/', defaults={'slug': ''})
@blueprint.route('/<slug>/')
def rst_content(slug):
    """Render database-backed reStructuredText content as HTML pages."""
    page = AboutPage.query.current.filter_by(
        slug=slug,
        active=True,
    ).first_or_404()
    return render_template('about/rst.html', page=page)
